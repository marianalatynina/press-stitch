from collections import defaultdict
from itertools import combinations, product

import renpy.exports as renpy
from renpy.display.im import Image, MatrixColor, matrix, Composite

# A list of all facial expressions for the dynamic displayables
all_expressions = set()

# Ghost matrix
GHOST_MATRIX = matrix.tint(0.5, 0.5, 2.0) * matrix.opacity(0.6)
TINT_MATRIX = matrix.tint(0.1, 0.0, 0.0)

class Pose:
    def __init__(self, size, expr_pos):
        self.size = size
        self.expr_pos = expr_pos

class Mutation:

    def __init__(self, name=None, group=None, depth=1, below=False):
        self.name = name
        self.group = group
        self.depth = depth
        self.below = below
        self.images = defaultdict(dict)

class Eye:

    def __init__(self, name):
        self.name = name
        self.images = defaultdict(dict)

class Expression:

    def __init__(self, pose_id, variant_id, image, eye_image=None):
        self.pose_id = pose_id
        self.variant_id = variant_id
        self.image = image
        self.eye_image = eye_image

class Body:

    def __init__(self, color, poses, mutations={}):
        self.color = color
        self.poses = poses

        self.mutations = mutations
        self.mutation_groups = defaultdict(set)

        # Populate default mutation groups and fill out remainder of mutation
        # metadata
        for mutation_name, mutation in self.mutations.items():
            if mutation.name is None:
                mutation.name = mutation_name
            if mutation.group is None:
                mutation.group = mutation_name
            self.mutation_groups[mutation.group].add(mutation_name)

        # Other
        self.expressions = defaultdict(dict)
        self.bases = defaultdict(dict)
        self.breasts = defaultdict(dict)
        self.eyes = defaultdict(dict)
        self.misc = {}

        # Composited images
        self.images = {}

    def add_base(self, fields, filename):
        if 'var' in fields:
            variant = fields.pop()
            if fields.pop() != 'var':
                renpy.error('Malformed filename "{0}"'.format(filename))
        else:
            variant = 0
        pose = int(fields.pop())
        self.bases[tuple(fields)][(pose, variant)] = Image(filename)

    def add_breast(self, level, fields, filename):
        pose = int(fields.pop())
        self.breasts[tuple(fields)][(pose, level)] = Image(filename)

    def add_eye(self, fields, filename):
        pose = int(fields.pop())
        name = fields.pop()

        if name not in self.eyes:
            self.eyes[name] = Eye(name)

        self.eyes[name].images[tuple(fields)][pose] = Image(filename)

    def add_mutation(self, fields, filename, below):
        pose = int(fields.pop())
        name = fields.pop()

        # Create mutation entry/add to group map if it doesn't already exist
        if name not in self.mutations:
            self.mutations[name] = Mutation(
                name=name,
                depth=1,
                group=name,
                below=below
            )
            self.mutation_groups[name].add(name)

        self.mutations[name].images[tuple(fields)][pose] = Image(filename)

    def add_expression(self, fields, filename):
        pose_id = int(fields.pop())

        # Get ID and attributes
        id = 0
        attribs = []
        while id == 0:
            field = fields.pop()
            if field.isdigit():
                id = int(field)
            else:
                attribs.insert(0, field)

        # TODO: get variant id
        name = (str(id),) + tuple(attribs)
        self.expressions[tuple(fields)][name] = Expression(pose_id, 0, Image(filename))
        all_expressions.add(name)

    def add_misc(self, fields, filename):
        self.misc[tuple(fields)] = Image(filename)

    def add_image(self, fields, filename):
        # Parse the type
        type = fields.pop(0)
        if type == 'base':
            self.add_base(fields, filename)
        elif type.startswith('be'):
            self.add_breast(int(type[2:]), fields, filename)
        elif type == 'eye':
            self.add_eye(fields, filename)
        elif type == 'mth':
            self.add_eye(fields, filename)
        elif type == 'mut':
            self.add_mutation(fields, filename, below=False)
        elif type == 'mutunder':
            self.add_mutation(fields, filename, below=True)
        elif type == 'ex':
            self.add_expression(fields, filename)
        elif type == 'misc':
            self.add_misc(fields, filename)
        else:
            renpy.error('Unknown character image type for "{0}"'.format(filename))

    ##################
    # Compose images #

    def define_images(self, image_tag, fold):
        # Generate args for mutations
        # mutation_args[path][name][pose] = image
        mutation_args = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
        for mutation_name, mutation in self.mutations.items():
            for mutation_path in mutation.images.keys():
                mutation_poses_list = self.match_all_paths(mutation.images, mutation_path, mutation.depth)

                # Append args per pose
                args_per_pose = mutation_args[mutation_path][mutation_name]
                for mutation_poses in mutation_poses_list:
                    for mutation_pose, image in mutation_poses.items():
                        args_per_pose[mutation_pose].append((0, 0))
                        args_per_pose[mutation_pose].append(image)

        # Compose images
        for base_path, base_images in self.bases.items():
            # Get list of expressions for this base
            expressions = self.match_first_path(self.expressions, base_path)
            if not expressions:
                continue

            # Get pose info
            poses = self.match_first_path(self.poses, base_path)
            if not poses:
                continue

            # Generate flash ('white') images
            for pose_id, __ in poses.items():
                name = (image_tag + 'flash',) + base_path + (str(pose_id),)
                image = base_images.get((pose_id, 0))
                if image:
                    renpy.image(name, self.flashimage(image))

            # Generate expression variants for eyes
            new_expressions = {}
            for eyename in self.eyes:
                eyes = self.match_first_path(self.eyes[eyename].images, base_path)
                if eyes:
                    for pose_id in eyes:
                        for expr_name, expr in expressions.items():
                            if expr.pose_id == pose_id:
                                new_name = expr_name + (eyename,)
                                new_expressions[new_name] = Expression(pose_id, expr.variant_id, expr.image, eyes[pose_id])
                                all_expressions.add(new_name)

            new_expressions.update(expressions)

            # Generate images for each expression
            for expr_name, expr in new_expressions.items():
                base_image = base_images[expr.pose_id, expr.variant_id]
                pose = poses[expr.pose_id]

                if isinstance(pose, Pose):
                    image_size = pose.size
                    expr_pos = pose.expr_pos
                else:
                    image_size = pose
                    expr_pos = (0, 0)

                base_image_args = (
                    (0, 0), base_image,
                    expr_pos, expr.image
                )

                if (expr.eye_image):
                    base_image_args = base_image_args + ((0, 0), expr.eye_image)

                # Find all the mutations that are available for this particular path,
                # and see if we should start with a minimum of 0 or 1 mutations.
                # Start with a minimum of 1 if we have a mutation named ''.
                mutation_start = 0
                mutations = self.match_first_path(mutation_args, base_path)
                grouped_mutations = []
                if mutations:
                    for mutation_group in self.mutation_groups.values():
                        group = []
                        for mutation_name in mutation_group:
                            if mutation_name in mutations:
                                group.append(mutation_name)

                                if self.mutations[mutation_name].name == '':
                                    mutation_start = 1
                        if group:
                            grouped_mutations.append(group)

                # Iterate over the mutations
                for i in range(mutation_start, len(grouped_mutations)+1):
                    for mutation_sets in combinations(grouped_mutations, i):
                        for mutation_names in product(*mutation_sets):

                            initial_image_args = [image_size]
                            mut_image_args = list(base_image_args)
                            mut_image_name = []

                            for mutation_name in mutation_names:
                                if self.mutations[mutation_name].below:
                                    initial_image_args.extend(mutations[mutation_name][expr.pose_id])
                                else:
                                    mut_image_args.extend(mutations[mutation_name][expr.pose_id])

                                # Append name to image tags
                                if self.mutations[mutation_name].name != '':
                                    mut_image_name.append(self.mutations[mutation_name].name)

                            mut_image_name = tuple(mut_image_name)

                            def define_be(be_level, be_image):
                                if be_image is None:
                                    be_image_args = mut_image_args
                                else:
                                    be_image_args = list(mut_image_args)
                                    be_image_args.append((0, 0))
                                    be_image_args.append(be_image)

                                if be_level == 0:
                                    be_image_name = ()
                                else:
                                    be_image_name = ('be' + str(be_level),)

                                # Define images
                                image_name = self.fold_name(base_path + be_image_name + mut_image_name + expr_name, fold)
                                composite_image_args = []
                                composite_image_args.extend(initial_image_args)
                                composite_image_args.extend(be_image_args)
                                image = Composite(*composite_image_args)
                                self.images[frozenset(image_name)] = image

                                renpy.image((image_tag,) + image_name, image)
                                image_ghost = MatrixColor(image, GHOST_MATRIX)
                                renpy.image((image_tag + 'ghost',) + image_name, image_ghost)
                                image_tint = MatrixColor(image, TINT_MATRIX)
                                renpy.image((image_tag + 'tint',) + image_name, image_tint)

                            # Iterate over BE
                            breasts = self.match_first_path(self.breasts, base_path)
                            if breasts:
                                if 0 not in breasts:
                                    define_be(0, None)
                                for (pose_id, be_level), image in breasts.items():
                                    if expr.pose_id != pose_id:
                                        continue
                                    define_be(be_level, image)
                            else:
                                define_be(0, None)

        # Now define misc images
        for misc_name, misc_image in self.misc.items():
            renpy.image((image_tag,) + misc_name, misc_image)
            renpy.image((image_tag + 'flash',) + misc_name, self.flashimage(misc_image))

    @staticmethod
    def flashimage(image):
        return MatrixColor(image, matrix.tint(0.1, 0.0, 0.0))

    @staticmethod
    def fold_name(name, fold):
        result = list(name)
        for attribs, sub in fold:
            if isinstance(attribs, str):
                try:
                    if sub:
                        result[result.index(attribs)] = sub
                    else:
                        result.remove(attribs)
                except ValueError:
                    pass
            elif isinstance(attribs, frozenset):
                if attribs.issubset(result):
                    for i, attrib in enumerate(attribs):
                        if i == 0:
                            result[result.index(attrib)] = sub
                        else:
                            result.remove(attrib)
        return tuple(result)

    @staticmethod
    def match_first_path(d, path):
        key = list(path)
        while True:
            tup = tuple(key)
            if tup in d:
                return d[tup]
            if not key:
                return None
            key.pop()

    @staticmethod
    def match_all_paths(d, path, depth=0):
        result = []

        key = list(path)
        while True:
            tup = tuple(key)
            if tup in d:
                result.append(d[tup])
                if depth > 0 and len(result) == depth:
                    break
            if not key:
                break
            key.pop()

        return result

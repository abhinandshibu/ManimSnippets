# class LinearTransformationExample(LinearTransformationScene):
#     CONFIG = {
#         "leave_ghost_vectors": True,
#     }
#     def construct(self):
#         matrix = [[1, 1], [0, 1]] #Shear
#         object = Dot(color = YELLOW)
#         self.add(object)
#         self.apply_matrix(matrix)
#         self.wait()
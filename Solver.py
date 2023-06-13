import math

import numpy as np

from Board import Board, Node


class Algorithms:
    def __init__(self):
        self.expanded_nodes = 0

    # alpha beta algorithm
    def minimax_alpha_beta(self, node, depth, alpha, beta, maximizing_player):
        if maximizing_player:
            node.children = node.value.create_children("X")
            self.expanded_nodes += len(node.children)
        else:
            node.children = node.value.create_children("O")
            self.expanded_nodes += len(node.children)

        if depth == 0 or node.is_leaf():
            return node.value

        if maximizing_player:
            value = -math.inf

            for child in node.children:
                if value == -math.inf:
                    value = self.minimax_alpha_beta(child, depth - 1, alpha, beta, False)
                else:
                    temp = self.minimax_alpha_beta(child, depth - 1, alpha, beta, False)
                    if temp.get_utility() > value.get_utility():
                        value = temp

                if alpha == -math.inf or value.get_utility() > alpha.get_utility():
                    alpha = value

                if alpha != -math.inf and beta != math.inf and alpha.get_utility() >= beta.get_utility():
                    break
            return value
        else:
            value = math.inf
            for child in node.children:
                if (value == math.inf):
                    value = self.minimax_alpha_beta(child, depth - 1, alpha, beta, True)
                else:
                    temp = self.minimax_alpha_beta(child, depth - 1, alpha, beta, True)
                    if (temp.get_utility() < value.get_utility()):
                        value = temp

                if (beta == math.inf or value.get_utility() < beta.get_utility()):
                    beta = value

                if alpha != -math.inf and beta != math.inf and alpha.get_utility() >= beta.get_utility():
                    break
            return value

    # minimax algorithm
    def minimax(self, node, depth, maximizing_player):
        if maximizing_player:

            node.children = node.value.create_children("O")
            self.expanded_nodes += len(node.children)
        else:

            node.children = node.value.create_children("X")
            self.expanded_nodes += len(node.children)

        if depth == 0 or node.is_leaf():
            return node.value

        if maximizing_player:
            value = -math.inf

            for child in node.children:

                if value == -math.inf:
                    value = self.minimax(child, depth - 1, False)
                    continue
                else:
                    temp = self.minimax(child, depth - 1, False)
                    if temp.get_utility() > value.get_utility():
                        value = temp

            return value
        else:
            value = math.inf
            for child in node.children:

                if value == math.inf:
                    value = self.minimax(child, depth - 1, True)
                    continue
                else:
                    temp = self.minimax(child, depth - 1, True)
                    if temp.get_utility() < value.get_utility():
                        value = temp
            return value

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from models.modules.linear import MVLinear
from models.modules.mvlayernorm import MVLayerNorm

class SelfAttentionClifford(nn.Module):
    def __init__(self, num_feat, num_nodes, num_edges, algebra):
        super(SelfAttentionClifford, self).__init__()
        self.num_feat = num_feat
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.algebra = algebra
        self.q_linear = MVLinear(algebra, num_feat, 1, subspaces=True)
        self.k_linear = MVLinear(algebra, num_feat, 1, subspaces=True)
        self.v_linear = MVLinear(algebra, num_feat, 1, subspaces=True)
        self.output_embedding = MVLinear(algebra, 1*2, num_feat, subspaces=True)
        self.concat_layernorm = MVLayerNorm(algebra, 2)

    def forward(self, feature_matrix):
        bs = feature_matrix.size(0)//25

        # Compute query, key, and value matrices
        q = self.q_linear(feature_matrix)
        k = self.k_linear(feature_matrix)
        v = self.v_linear(feature_matrix)

        # Compute dot product for attention
        q1_reshape = q.view(25*bs, -1)
        k1_reshape = k.view(25*bs, -1)

        attn = torch.mm(q1_reshape, k1_reshape.T)  # (bs*(num_nodes + num_edges), num_feat, 8)
        # Normalize the attention weights with d normally
        attn = attn / math.sqrt(k.size(-1))
        attn = F.softmax(attn, dim=-1)

        v_reshaped = v.squeeze(1)
        attention_feature_matrix = torch.matmul(attn, v_reshaped)
        attention_feature_matrix = attention_feature_matrix.unsqueeze(1)

        # Apply geometric product but might not be necessary let's check with Cong.
        gp_feature_matrix = self.geometric_product(attention_feature_matrix, attention_feature_matrix)

        concat_feature_matrix = torch.cat((attention_feature_matrix, gp_feature_matrix), dim=1)
        normalized_concat_feature_matrix = self.concat_layernorm(concat_feature_matrix)
        embed_output = self.output_embedding(normalized_concat_feature_matrix)

        return embed_output

    def geometric_product(self, a, b):
        return self.algebra.geometric_product(a, b)

class GAST_block(nn.Module):
    def __init__(self, d_model, num_heads, clifford_algebra, channels):
        super(GAST_block, self).__init__()
        self.mvlayernorm = MVLayerNorm(clifford_algebra, channels)
        self.self_attn = SelfAttentionClifford(7, 5, 20, clifford_algebra)

    def forward(self, src, src_mask=None):
        src = self.mvlayernorm(src)
        src = self.self_attn(src)
        return src

class GAST(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, clifford_algebra, channels):
        super(GAST, self).__init__()
        self.layers = nn.ModuleList(
            [GAST_block(d_model, num_heads, clifford_algebra, channels) for _ in range(num_layers)])

    def forward(self, src, src_mask=None):
        for layer in self.layers:
            src = layer(src, src_mask)
        return src
# the most imfamous word classifier.
import networkx as nx
from itertools import tee
# I have found volunarbilities in Baidu!
# one can only bookmark the page to get the real fucking link!
# import matplotlib.pyplot as plt
# have weighted graph but never fucking mind.
# the most invisible break among those things.
# shall we use circuit analyzer or physics to do the task?
def pairwise(_iterable):
  "s -> (s0,s1), (s1,s2), (s2, s3), ..."
  a, b = tee(_iterable)
  next(b, None)
  return zip(a, b)
def shatter(a):
  return [x for x in a]
def getFucked(a, b):
  for x, y in pairwise(a):
    b.add_edge(x, y)
  return b
G = nx.MultiDiGraph() # just fuck.
ap=['AmbiguousSolution', 'DiGraph', 'ExceededMaxIterations', 'Graph', 'GraphMLReader', 'GraphMLWriter', 'HasACycle', 'LCF_graph', 'MultiDiGraph', 'MultiGraph', 'NetworkXAlgorithmError', 'NetworkXError', 'NetworkXException', 'NetworkXNoCycle', 'NetworkXNoPath', 'NetworkXNotImplemented', 'NetworkXPointlessConcept', 'NetworkXTreewidthBoundExceeded', 'NetworkXUnbounded', 'NetworkXUnfeasible', 'NodeNotFound', 'NotATree', 'OrderedDiGraph', 'OrderedGraph', 'OrderedMultiDiGraph', 'OrderedMultiGraph', 'PlanarEmbedding', 'PowerIterationFailedConvergence', '__author__', '__bibtex__', '__builtins__', '__cached__', '__date__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'absolute_import', 'adamic_adar_index', 'add_cycle', 'add_path', 'add_star', 'adj_matrix', 'adjacency', 'adjacency_data', 'adjacency_graph', 'adjacency_matrix', 'adjacency_spectrum', 'adjlist', 'algebraic_connectivity', 'algebraicconnectivity', 'algorithms', 'all', 'all_neighbors', 'all_node_cuts', 'all_pairs_bellman_ford_path', 'all_pairs_bellman_ford_path_length', 'all_pairs_dijkstra', 'all_pairs_dijkstra_path', 'all_pairs_dijkstra_path_length', 'all_pairs_lowest_common_ancestor', 'all_pairs_node_connectivity', 'all_pairs_shortest_path', 'all_pairs_shortest_path_length', 'all_shortest_paths', 'all_simple_paths', 'all_topological_sorts', 'ancestors', 'antichains', 'approximate_current_flow_betweenness_centrality', 'articulation_points', 'assortativity', 'astar', 'astar_path', 'astar_path_length', 'atlas', 'attr_matrix', 'attr_sparse_matrix', 'attracting', 'attracting_component_subgraphs', 'attracting_components', 'attribute_assortativity_coefficient', 'attribute_mixing_dict', 'attribute_mixing_matrix', 'attrmatrix', 'authority_matrix', 'average_clustering', 'average_degree_connectivity', 'average_neighbor_degree', 'average_node_connectivity', 'average_shortest_path_length', 'balanced_tree', 'barabasi_albert_graph', 'barbell_graph', 'beamsearch', 'bellman_ford_path', 'bellman_ford_path_length', 'bellman_ford_predecessor_and_distance', 'betweenness', 'betweenness_centrality', 'betweenness_centrality_source', 'betweenness_centrality_subset', 'betweenness_subset', 'bfs_beam_edges', 'bfs_edges', 'bfs_predecessors', 'bfs_successors', 'bfs_tree', 'biconnected', 'biconnected_component_edges', 'biconnected_component_subgraphs', 'biconnected_components', 'bidirectional_dijkstra', 'bidirectional_shortest_path', 'binary', 'binomial_graph', 'bipartite', 'bipartite_layout', 'boundary', 'boundary_expansion', 'breadth_first_search', 'bridges', 'bull_graph', 'capacity_scaling', 'cartesian_product', 'caveman_graph', 'center', 'centrality', 'chain_decomposition', 'chains', 'check_planarity', 'chordal', 'chordal_cycle_graph', 'chordal_graph_cliques', 'chordal_graph_treewidth', 'chvatal_graph', 'circulant_graph', 'circular_ladder_graph', 'circular_layout', 'classes', 'classic', 'clique', 'cliques_containing_node', 'closeness', 'closeness_centrality', 'closeness_vitality', 'cluster', 'clustering', 'cn_soundarajan_hopcroft', 'coloring', 'combinatorial_embedding_to_pos', 'common_neighbors', 'communicability', 'communicability_alg', 'communicability_betweenness_centrality', 'communicability_exp', 'community', 'complement', 'complete_bipartite_graph', 'complete_graph', 'complete_multipartite_graph', 'components', 'compose', 'compose_all', 'condensation', 'conductance', 'configuration_model', 'connected', 'connected_caveman_graph', 'connected_component_subgraphs', 'connected_components', 'connected_double_edge_swap', 'connected_watts_strogatz_graph', 'connectivity', 'constraint', 'contracted_edge', 'contracted_nodes', 'convert', 'convert_matrix', 'convert_node_labels_to_integers', 'core', 'core_number', 'coreviews', 'correlation', 'cost_of_flow', 'could_be_isomorphic', 'covering', 'create_empty_copy', 'cubical_graph', 'current_flow_betweenness', 'current_flow_betweenness_centrality', 'current_flow_betweenness_centrality_subset', 'current_flow_betweenness_subset', 'current_flow_closeness', 'current_flow_closeness_centrality', 'cut_size', 'cuts', 'cycle_basis', 'cycle_graph', 'cycles', 'cytoscape', 'cytoscape_data', 'cytoscape_graph', 'dag', 'dag_longest_path', 'dag_longest_path_length', 'dag_to_branching', 'davis_southern_women_graph','degree', 'degree_alg', 'degree_assortativity_coefficient', 'degree_centrality', 'degree_histogram', 'degree_mixing_dict', 'degree_mixing_matrix', 'degree_pearson_correlation_coefficient', 'degree_seq', 'degree_sequence_tree', 'dense', 'dense_gnm_random_graph', 'density', 'depth_first_search', 'desargues_graph', 'descendants', 'dfs_edges', 'dfs_labeled_edges', 'dfs_postorder_nodes', 'dfs_predecessors', 'dfs_preorder_nodes', 'dfs_successors', 'dfs_tree', 'diameter', 'diamond_graph', 'difference', 'digraph', 'dijkstra_path', 'dijkstra_path_length', 'dijkstra_predecessor_and_distance', 'directed', 'directed_combinatorial_laplacian_matrix', 'directed_configuration_model', 'directed_havel_hakimi_graph', 'directed_laplacian_matrix', 'directed_modularity_matrix', 'disjoint_union', 'disjoint_union_all', 'dispersion', 'distance_measures', 'distance_regular', 'dodecahedral_graph', 'dominance', 'dominance_frontiers', 'dominating', 'dominating_set', 'dorogovtsev_goltsev_mendes_graph', 'double_edge_swap', 'draw', 'draw_circular', 'draw_kamada_kawai', 'draw_networkx', 'draw_networkx_edge_labels', 'draw_networkx_edges', 'draw_networkx_labels', 'draw_networkx_nodes', 'draw_planar', 'draw_random', 'draw_shell', 'draw_spectral', 'draw_spring', 'drawing', 'dual_barabasi_albert_graph', 'duplication', 'duplication_divergence_graph', 'eccentricity', 'edge_betweenness', 'edge_betweenness_centrality', 'edge_betweenness_centrality_subset', 'edge_bfs', 'edge_boundary', 'edge_connectivity', 'edge_current_flow_betweenness_centrality', 'edge_current_flow_betweenness_centrality_subset','edge_dfs', 'edge_disjoint_paths', 'edge_expansion', 'edge_load_centrality', 'edge_subgraph', 'edgebfs', 'edgedfs', 'edgelist', 'edges', 'effective_size', 'efficiency', 'ego','ego_graph', 'eigenvector', 'eigenvector_centrality', 'eigenvector_centrality_numpy', 'empty_graph', 'enumerate_all_cliques', 'equitable_color', 'erdos_renyi_graph', 'estrada_index', 'euler', 'eulerian_circuit', 'eulerize', 'exception', 'expanders', 'expected_degree_graph', 'extended_barabasi_albert_graph', 'extrema_bounding', 'fast_could_be_isomorphic', 'fast_gnp_random_graph', 'faster_could_be_isomorphic', 'fiedler_vector', 'filters', 'find_cliques', 'find_cliques_recursive', 'find_cores', 'find_cycle', 'find_induced_nodes', 'florentine_families_graph', 'flow', 'flow_hierarchy', 'flow_matrix', 'floyd_warshall', 'floyd_warshall_numpy', 'floyd_warshall_predecessor_and_distance', 'freeze', 'from_dict_of_dicts', 'from_dict_of_lists', 'from_edgelist', 'from_graph6_bytes', 'from_nested_tuple', 'from_numpy_array', 'from_numpy_matrix', 'from_pandas_adjacency', 'from_pandas_edgelist', 'from_prufer_sequence', 'from_scipy_sparse_matrix', 'from_sparse6_bytes', 'frucht_graph', 'fruchterman_reingold_layout', 'full_rary_tree', 'function', 'gaussian_random_partition_graph', 'general_random_intersection_graph', 'generalized_degree', 'generate_adjlist', 'generate_edgelist', 'generate_gexf', 'generate_gml', 'generate_graphml', 'generate_multiline_adjlist', 'generate_pajek', 'generators', 'generic', 'geographical_threshold_graph', 'geometric', 'get_edge_attributes', 'get_node_attributes', 'gexf', 'global_efficiency', 'global_parameters', 'global_reaching_centrality', 'gml', 'gn_graph', 'gnc_graph', 'gnm_random_graph', 'gnp_random_graph', 'gnr_graph', 'goldberg_radzik', 'gomory_hu_tree', 'google_matrix', 'gpickle', 'graph', 'graph6', 'graph_atlas', 'graph_atlas_g', 'graph_clique_number', 'graph_edit_distance', 'graph_number_of_cliques', 'graphical', 'graphmatrix', 'graphml', 'graphviews', 'greedy_color', 'grid_2d_graph', 'grid_graph','harmonic', 'harmonic_centrality', 'has_bridges', 'has_path', 'havel_hakimi_graph', 'heawood_graph', 'hexagonal_lattice_graph', 'hierarchy', 'hits', 'hits_alg', 'hits_numpy', 'hits_scipy', 'hoffman_singleton_graph', 'house_graph', 'house_x_graph', 'hub_matrix', 'hybrid', 'hypercube_graph', 'icosahedral_graph', 'identified_nodes', 'immediate_dominators', 'in_degree_centrality', 'incidence_matrix', 'induced_subgraph', 'info', 'information_centrality', 'intersection', 'intersection_all', 'intersection_array', 'inverse_line_graph', 'is_aperiodic', 'is_arborescence', 'is_attracting_component', 'is_biconnected', 'is_bipartite', 'is_branching', 'is_chordal', 'is_connected', 'is_digraphical', 'is_directed', 'is_directed_acyclic_graph', 'is_distance_regular', 'is_dominating_set', 'is_edge_cover', 'is_empty', 'is_eulerian', 'is_forest', 'is_frozen', 'is_graphical', 'is_isolate', 'is_isomorphic', 'is_k_edge_connected', 'is_kl_connected', 'is_matching', 'is_maximal_matching', 'is_multigraphical', 'is_negatively_weighted', 'is_perfect_matching', 'is_pseudographical', 'is_semiconnected', 'is_simple_path', 'is_strongly_connected', 'is_strongly_regular', 'is_tree', 'is_valid_degree_sequence_erdos_gallai', 'is_valid_degree_sequence_havel_hakimi', 'is_valid_joint_degree', 'is_weakly_connected', 'is_weighted', 'isolate', 'isolates', 'isomorphism', 'jaccard_coefficient', 'jit', 'jit_data', 'jit_graph', 'johnson', 'join', 'joint_degree_graph', 'joint_degree_seq', 'json_graph', 'k_components', 'k_core', 'k_corona', 'k_crust', 'k_edge_augmentation', 'k_edge_components', 'k_edge_subgraphs', 'k_nearest_neighbors', 'k_random_intersection_graph', 'k_shell', 'kamada_kawai_layout', 'karate_club_graph', 'katz', 'katz_centrality', 'katz_centrality_numpy', 'kl_connected_subgraph', 'kosaraju_strongly_connected_components', 'krackhardt_kite_graph', 'ladder_graph', 'laplacian_matrix', 'laplacian_spectrum', 'laplacianmatrix', 'lattice', 'lattice_reference', 'layout', 'leda', 'les_miserables_graph', 'lexicographic_product', 'lexicographical_topological_sort', 'linalg', 'line', 'line_graph', 'link_analysis', 'link_prediction', 'load', 'load_centrality', 'local_bridges', 'local_constraint', 'local_efficiency', 'local_reaching_centrality', 'lollipop_graph', 'lowest_common_ancestor', 'lowest_common_ancestors', 'make_clique_bipartite', 'make_max_clique_graph', 'make_small_graph', 'margulis_gabber_galil_graph', 'matching', 'max_flow_min_cost', 'max_weight_matching', 'maximal_independent_set', 'maximal_matching', 'maximum_branching', 'maximum_flow','maximum_flow_value', 'maximum_spanning_arborescence', 'maximum_spanning_edges', 'maximum_spanning_tree', 'min_cost_flow', 'min_cost_flow_cost', 'min_edge_cover', 'minimum_branching', 'minimum_cut', 'minimum_cut_value', 'minimum_cycle_basis', 'minimum_edge_cut', 'minimum_node_cut', 'minimum_spanning_arborescence', 'minimum_spanning_edges', 'minimum_spanning_tree', 'minors', 'mis', 'mixing', 'mixing_dict', 'mixing_expansion', 'modularity_matrix', 'modularity_spectrum', 'modularitymatrix', 'moebius_kantor_graph', 'multi_source_dijkstra', 'multi_source_dijkstra_path', 'multi_source_dijkstra_path_length', 'multidigraph', 'multigraph', 'multiline_adjlist', 'mycielski', 'mycielski_graph', 'mycielskian', 'navigable_small_world_graph', 'negative_edge_cycle', 'neighbor_degree', 'neighbors', 'network_simplex', 'networkx', 'newman_watts_strogatz_graph', 'node_attribute_xy', 'node_boundary', 'node_classification', 'node_clique_number', 'node_connected_component', 'node_connectivity', 'node_degree_xy', 'node_disjoint_paths', 'node_expansion', 'node_link', 'node_link_data', 'node_link_graph', 'nodes', 'nodes_with_selfloops', 'non_edges', 'non_neighbors', 'nonisomorphic_trees', 'normalized_cut_size', 'normalized_laplacian_matrix', 'normalized_laplacian_spectrum', 'not_implemented_for', 'null_graph', 'number_attracting_components', 'number_connected_components', 'number_of_cliques', 'number_of_edges', 'number_of_isolates', 'number_of_nodes', 'number_of_nonisomorphic_trees', 'number_of_selfloops', 'number_strongly_connected_components', 'number_weakly_connected_components','numeric_assortativity_coefficient', 'numeric_mixing_matrix', 'nx', 'nx_agraph', 'nx_pydot', 'nx_pylab', 'nx_shp', 'nx_yaml', 'octahedral_graph', 'omega', 'operators', 'optimal_edit_paths', 'optimize_edit_paths', 'optimize_graph_edit_distance', 'ordered', 'out_degree_centrality', 'overall_reciprocity', 'pagerank', 'pagerank_alg', 'pagerank_numpy', 'pagerank_scipy', 'pairs', 'pajek', 'pappus_graph', 'parse_adjlist', 'parse_edgelist', 'parse_gml', 'parse_graphml', 'parse_leda', 'parse_multiline_adjlist', 'parse_pajek', 'partial_duplication_graph', 'path_graph', 'percolation', 'percolation_centrality', 'periphery', 'petersen_graph', 'planar_drawing', 'planar_layout', 'planarity', 'planted_partition_graph', 'power', 'powerlaw_cluster_graph', 'predecessor', 'preferential_attachment', 'prefix_tree', 'product', 'project', 'projected_graph', 'quotient_graph', 'ra_index_soundarajan_hopcroft', 'radius', 'random_clustered', 'random_clustered_graph', 'random_degree_sequence_graph', 'random_geometric_graph', 'random_graphs', 'random_k_out_graph', 'random_kernel_graph', 'random_layout', 'random_lobster', 'random_partition_graph', 'random_powerlaw_tree', 'random_powerlaw_tree_sequence', 'random_reference', 'random_regular_graph', 'random_shell_graph', 'random_tree', 'reaching', 'read_adjlist', 'read_edgelist', 'read_gexf', 'read_gml', 'read_gpickle', 'read_graph6', 'read_graphml', 'read_leda', 'read_multiline_adjlist', 'read_pajek', 'read_shp', 'read_sparse6', 'read_weighted_edgelist','read_yaml', 'readwrite', 'reciprocity', 'reconstruct_path', 'recursive_simple_cycles','relabel', 'relabel_gexf_graph', 'relabel_nodes', 'relaxed_caveman_graph', 'release', 'reportviews', 'rescale_layout', 'resource_allocation_index', 'restricted_view', 'reverse', 'reverse_view', 'rich_club_coefficient', 'richclub', 'ring_of_cliques', 'rooted_product', 's_metric', 'scale_free_graph', 'second_order', 'second_order_centrality', 'sedgewick_maze_graph', 'selfloop_edges', 'semiconnected', 'set_edge_attributes', 'set_node_attributes', 'shell_layout', 'shortest_path', 'shortest_path_length', 'shortest_paths', 'shortest_simple_paths', 'sigma', 'similarity', 'simple_cycles', 'simple_paths', 'single_source_bellman_ford', 'single_source_bellman_ford_path', 'single_source_bellman_ford_path_length', 'single_source_dijkstra', 'single_source_dijkstra_path', 'single_source_dijkstra_path_length', 'single_source_shortest_path', 'single_source_shortest_path_length', 'single_target_shortest_path', 'single_target_shortest_path_length', 'small', 'smallworld', 'smetric', 'social', 'soft_random_geometric_graph', 'spanner', 'sparse6', 'sparsifiers','spectral_graph_forge', 'spectral_layout', 'spectral_ordering', 'spectrum', 'spring_layout', 'square_clustering', 'star_graph', 'stochastic', 'stochastic_block_model', 'stochastic_graph', 'stoer_wagner', 'strong_product', 'strongly_connected', 'strongly_connected_component_subgraphs', 'strongly_connected_components', 'strongly_connected_components_recursive', 'structuralholes', 'subgraph', 'subgraph_alg', 'subgraph_centrality', 'subgraph_centrality_exp', 'swap', 'symmetric_difference', 'tensor_product', 'test', 'tests', 'tetrahedral_graph', 'thresholded_random_geometric_graph', 'to_dict_of_dicts', 'to_dict_of_lists', 'to_directed', 'to_edgelist', 'to_graph6_bytes', 'to_nested_tuple', 'to_networkx_graph', 'to_numpy_array', 'to_numpy_matrix', 'to_numpy_recarray', 'to_pandas_adjacency', 'to_pandas_edgelist', 'to_prufer_sequence', 'to_scipy_sparse_matrix', 'to_sparse6_bytes', 'to_undirected', 'topological_sort', 'tournament', 'transitive_closure', 'transitive_reduction', 'transitivity', 'traversal', 'tree', 'tree_all_pairs_lowest_common_ancestor', 'tree_data', 'tree_graph', 'trees', 'triad_graph', 'triadic_census', 'triads', 'triangles', 'triangular_lattice_graph', 'trivial_graph', 'truncated_cube_graph', 'truncated_tetrahedron_graph', 'turan_graph', 'tutte_graph', 'unary', 'uniform_random_intersection_graph', 'union', 'union_all', 'unweighted', 'utils', 'vitality', 'volume', 'voronoi', 'voronoi_cells', 'voterank', 'voterank_alg', 'watts_strogatz_graph', 'waxman_graph', 'weakly_connected', 'weakly_connected_component_subgraphs', 'weakly_connected_components', 'weighted', 'wheel_graph', 'wiener', 'wiener_index', 'windmill_graph', 'within_inter_cluster', 'write_adjlist', 'write_edgelist', 'write_gexf', 'write_gml', 'write_gpickle', 'write_graph6', 'write_graphml', 'write_graphml_lxml', 'write_graphml_xml', 'write_multiline_adjlist', 'write_pajek', 'write_shp', 'write_sparse6', 'write_weighted_edgelist', 'write_yaml']
# fuck me.
f,s1=0,None
for g0 in ap:
  s0=shatter(g0)
  if f==0:
    s1=getFucked(s0,G)
  else:
    s1=getFucked(s0,s1)
nx.write_gpickle(s1,"noneTheLess.gpickle")
# how the fuck can we read this fuck?
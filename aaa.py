"""
BEHAVIOURAL ANALYSES
"""

seaborn.set_style(style='white')

params['acc_simu'] = 1  # how accurate simulated node/edge agent is
recent = -1  # how far back into history of saved data
filt_size = 61  # smoothing window size (must be odd)
n = 10
fracs = [x /n for x in range(n+2)]  # for assessing accuracy within certain proportions of nodes visited

# for steps since visted analysis - assess accuracy within those steps
if params['world_type'] in ['family_tree', 'line_ti', 'tonegawa']:
    a_s = [0, 10, 20]
else:
    a_s = [0, 4, 10, 20, 40, 60, 100, 200, 300, 400, 600]

# Load data
positions_link, coos, env_info, distance_info = link_inferences(save_path, list_of_files, widths, batch_id, params,\
                                                                index=recent)
n_states, wids, n_available_states, n_available_edges = env_info

# Perform behavioural analayses. Partition results into environments of same size
allowed_widths = sorted(np.unique([widths[b_id] for b_id in batch_id]))
results = []
for allowed_wid in allowed_widths:
    p_cors, nodes_visited_all, edges_visited_all, time_vis_anal = \
        analyse_link_inference(allowed_wid, fracs, a_s, positions_link, coos, env_info, params)
    p_cors = [ind for ind in p_cors if len(ind)>0]
    results.append([p_cors, nodes_visited_all, edges_visited_all, time_vis_anal])
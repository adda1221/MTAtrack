from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/root/projects/MTAtrack/data/got10k_lmdb'
    settings.got10k_path = '/root/projects/TransT/data/GOT10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_lmdb_path = '/root/projects/MTAtrack/data/lasot_lmdb'
    settings.lasot_path = '/root/projects/TransT/data/Lasot/LaSOTBenchmark'
    settings.network_path = '/root/projects/MTAtrack/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = ''
    settings.otb_path = ''
    settings.prj_dir = '/root/projects/MTAtrack'
    settings.result_plot_path = '/root/projects/MTAtrack/test/result_plots'
    settings.results_path = '/root/projects/MTAtrack/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/root/projects/MTAtrack'
    settings.segmentation_path = '/root/projects/MTAtrack/test/segmentation_results'
    settings.tn_packed_results_path = ''
    settings.tpl_path = ''
    settings.trackingnet_path = '/root/projects/TransT/data/TrackingNet'
    settings.uav_path = ''
    settings.vot_path = '/root/projects/MTAtrack/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings


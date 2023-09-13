import resources.selfspy.selfspy.stats as stats

DATADIR = os.path.expanduser(stats.cfg.DATA_DIR)
DBPATH = os.path.join(DATADIR, stats.cfg.DBNAME)
ARGS = {
    'config': None,
    'password': None,
    'data_dir': DATADIR,
    'showtext': False,
    'date': None,
    'clock': None,
    'id': None,
    'back': None,
    'limit': None,
    'min_keys': None,
    'title': None,
    'process': None,
    'body': None,
    'clicks': False,
    'key_freqs': False,
    'human_readable': False,
    'active': None,
    'ratios': None,
    'periods': None,
    'pactive': None,
    'tactive': None,
    'pkeys': False,
    'tkeys': False
}


def ratios(cutoff, back):
    ARGS['ratios'] = cutoff
    ARGS['back'] = back
    s = stats.Selfstats(DBPATH, ARGS)
    s.calc_summary()
    s.show_summary()

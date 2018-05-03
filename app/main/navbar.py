class NavBar(object):
    # TODO: Documentation
    menus = {
        'IOCs': (
            'Indicators',
            'Low and Slows'
        ),
        'Compliance': (
            'By Site',
            'By POR'
        ),
        'Reports': (
            'Daily',
            'Quarterly'
        ),
        'Analyst': (
            'Scanners',
            'Scans',
            'Scheduled Scans',
            'Scan Results',
            'IAVMs'
        ),
        'Program Support': (
            'Users',
            'Groups'
        ),
        'Cyber Hunt': (
            {
                'IOC Tracker': (
                    'Windows',
                    'Linux',
                    'Mac'
                )
            },
            {
                'Attack Matrix': (
                    'Windows',
                    'Linux',
                    'Mac'
                )
            },
            'Query Status'
        ),
        'Duty Book': (None),
        'User Metrics': (None),
        'Subscriber': (None),
        'Ticketing': (None),
        'Tools': (None)
    }

    # TODO: Documentation
    def is_empty(self, menu):
        if self.menus[menu] is None:
            return True
        else:
            return False

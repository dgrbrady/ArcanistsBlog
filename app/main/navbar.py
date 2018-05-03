class NavBar(object):
    """Objects from this class hold a dict of items to populate the navigation bar.

    Class attributes:
        'menus' - dict:
            Each key represents what is going to be displayed on the
            navigation bar and for the purposes of this documentation will be
            referred to as 'menus'. Every menu requires a tuple containin
            their sub-menus. If no sub-menu is required, the tuple must
            explicitely contain the None value. If a sub-menu has a sub-menu,
            it must be represented as a dict with the key being the value you
            want displayed in the parent sub-menu and the value being a tuple
            containing the child sub-menu.

    Class methods:
        is_empty():
            Given a menu (key), the function will return true if the sub-menu
            (value) is None.
    """

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

    def is_empty(self, menu):
        """Pass a menu as a string to check if the menu contains any sub-menus.

        :param self: instance of NavBar.
        :param menu: *string* menu item to be evaluated.

        :returns: *bool* True if menu is empty, else returns False.
        """

        if self.menus[menu] is None:
            return True
        else:
            return False

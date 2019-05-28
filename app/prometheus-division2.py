#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import time
from prometheus_client import Gauge
from prometheus_client import start_http_server


class D2():

    """ Division2 class which get user information. """

    def __init__(self, url):
        self.url = url

    def get_user_id(self, uplay_name):
        params = (
            ('name', uplay_name),
            ('platform', 'uplay'),
        )
        try:
            r = requests.get(
                    self.url,
                    params=params
            )
        except Exception as e:
            return False
        else:
            if 'results' in r.json():
                return r.json()['results'][0]['user']
            else:
                return False

    def get_user_info(self, user_id):
        params = (
            ('pid', user_id),
        )
        try:
            r = requests.get(
                    self.url,
                    params=params
            )
        except Exception as e:
            return False, False, False, False, False, False, \
                   False, False, False, False, False, False, \
                   False, False, False, False, False, False, \
                   False
        else:
            timeplayed_total = int(r.json()['timeplayed_total'] / 3600)
            timeplayed_dz = int(r.json()['timeplayed_dz'] / 3600)
            timeplayed_pve = int(r.json()['timeplayed_pve'] / 3600)
            timeplayed_pvp = int(r.json()['timeplayed_pvp'] / 3600)
            timeplayed_rogue = int(r.json()['timeplayed_rogue'] / 3600)
            level_pve = r.json()['level_pve']
            level_dz = r.json()['level_dz']
            kills_npc = r.json()['kills_npc']
            kills_pvp = r.json()['kills_pvp']
            kills_pve_hyenas = r.json()['kills_pve_hyenas']
            kills_pve_outcasts = r.json()['kills_pve_outcasts']
            kills_pve_blacktusk = r.json()['kills_pve_blacktusk']
            kills_pve_truesons = r.json()['kills_pve_truesons']
            kills_pve_dz_hyenas = r.json()['kills_pve_dz_hyenas']
            kills_pve_dz_outcasts = r.json()['kills_pve_dz_outcasts']
            kills_pve_dz_blacktusk = r.json()['kills_pve_dz_blacktusk']
            kills_pve_dz_truesons = r.json()['kills_pve_dz_truesons']
            kills_headshot = r.json()['kills_headshot']
            headshots = r.json()['headshots']
            return timeplayed_total, timeplayed_dz, timeplayed_pve, \
                   timeplayed_pvp, timeplayed_rogue, level_pve, \
                   level_dz, kills_npc, kills_pvp, kills_pve_hyenas, \
                   kills_pve_outcasts, kills_pve_blacktusk, \
                   kills_pve_truesons, kills_pve_dz_hyenas, \
                   kills_pve_dz_outcasts, kills_pve_dz_blacktusk, \
                   kills_pve_dz_truesons, kills_headshot, headshots


def main():
    users = ['jedipigpig', 'gatchaman.jp', 'lobelia_dixon',
            'hayate_ewing', 'souyuh.jp']
    vars = ['timeplayed_total', 'timeplayed_dz',
            'timeplayed_pve', 'timeplayed_pvp',
            'timeplayed_rogue', 'level_pve',
            'level_dz', 'kills_npc',
            'kills_pvp', 'kills_pve_hyenas',
            'kills_pve_outcasts', 'kills_pve_blacktusk',
            'kills_pve_truesons', 'kills_pve_dz_hyenas',
            'kills_pve_dz_outcasts', 'kills_pve_dz_blacktusk',
            'kills_pve_dz_truesons', 'kills_headshot',
            'headshots']
    dict = {}
    for user in users:
        for var in vars:
            dict[user + '_' + var] = \
                    Gauge(user.replace('.', '_') + '_' + var, 'Gauge')

    start_http_server(8000)

    while True:
        for user in users:
            user_id = D2('https://thedivisiontab.com/api/search.php').get_user_id(user)
            value = D2('https://thedivisiontab.com/api/player.php').get_user_info(user_id)
            for var in vars:
                if user_id:
                    value_dict = {'timeplayed_total': value[0],
                            'timeplayed_dz': value[1], 'timeplayed_pve': value[2],
                            'timeplayed_pvp': value[3], 'timeplayed_rogue': value[4],
                            'level_pve': value[5], 'level_dz': value[6],
                            'kills_npc': value[7], 'kills_pvp': value[8],
                            'kills_pve_hyenas': value[9], 'kills_pve_outcasts': value[10],
                            'kills_pve_blacktusk': value[11], 'kills_pve_truesons': value[12],
                            'kills_pve_dz_hyenas': value[13], 'kills_pve_dz_outcasts': value[14],
                            'kills_pve_dz_blacktusk': value[15], 'kills_pve_dz_truesons': value[16],
                            'kills_headshot': value[17], 'headshots': value[18]}
                    dict[user + '_' + var].set(value_dict[var])
            time.sleep(60)


if __name__ == "__main__":
    main()

"""
Details for Overnight River Permits
"""
from dataclasses import dataclass

from river_skimmer.rivers.section import Section


@dataclass
class Permit:
    """
    Library of individual river sections
    """
    YampaDeerlodgePark = Section(
        id=250014,
        entrance=371,
        river='Yampa',
        name='Yampa',
        put_in='DeerlodgePark',
        take_out='SplitMountain',
    )
    GreenRiverDesolationGray = Section(
        id=233393,
        entrance=282,
        river='Green',
        name='DesolationGray',
        put_in='SandWash',
        take_out='Swaseys',
    )
    GreenRiverGatesOfLodore = Section(
        id=250014,
        entrance=380,
        river='Green',
        name='GatesOfLodore',
        put_in='Lodore',
        take_out='SplitMountain',
    )
    RubyHorsethief = Section(
        id=74466,
        entrance=None,
        river='Colorado',
        name='RubyHorsethief',
        put_in='MackLoma',
        take_out='Westwater',
    )
    Westwater = Section(
        id=621744,
        entrance=None,
        river='Colorado',
        name='Westwater',
        put_in='Westwater',
        take_out='Cisco',
    )
    SalmonMain = Section(
        id=234622,
        entrance=376,
        river='Salmon',
        name='MainSalmon',
        put_in='CornCreek',
        take_out='VinegarCreek',
    )
    SalmonMiddleFork = Section(
        id=234623,
        entrance=377,
        river='Salmon',
        name='MiddleForkSalmon',
        put_in='BoundaryCreek',
        take_out='CacheBar',
    )
    SanJuanMexicanHatClayHills = Section(
        id=250986,
        entrance=702,
        river='SanJuan',
        name='MexicanHatClayHills',
        put_in='MexicanHat',
        take_out='ClayHills',
    )
    SanJuanSandIslandClayHills = Section(
        id=250986,
        entrance=703,
        river='SanJuan',
        name='SandIslandClayHills',
        put_in='SandIsland',
        take_out='ClayHills',
    )
    SanJuanSandIslandMexicanHat = Section(
        id=250986,
        entrance=704,
        river='SanJuan',
        name='SandIslandMexicanHat',
        put_in='SandIsland',
        take_out='MexicanHat',
    )
    SnakeRiverHellsCanyon = Section(
        id=234625,
        entrance=379,
        river='Snake',
        name='HellsCanyon',
        put_in='HellsCanyonDam',
        take_out='HellerBar',
    )
    SelwayRiver = Section(
        id=234624,
        entrance=378,
        river='Selway',
        name='Selway',
        put_in='ParadiseCreek',
        take_out='RaceCreek',
    )
    RogueRiver = Section(
        id=251982,
        entrance=833,
        river='Rogue',
        name='RogueRiver',
        put_in='GraveCreek',
        take_out='FosterBar',
    )

    @property
    def river_sections(self):
        """
        Compiles a list of River Sections

        Returns:
            list: List of River Sections
        """
        return [
            self.GreenRiverDesolationGray,
            self.GreenRiverGatesOfLodore,
            # self.RubyHorsethief,  # Follows a different format on rec.gov
            # self.RogueRiver,  # Follows a different format on rec.gov
            # self.Westwater,  # Follows a different format on rec.gov
            self.SalmonMain,
            self.SalmonMiddleFork,
            self.SanJuanMexicanHatClayHills,
            self.SanJuanSandIslandClayHills,
            self.SanJuanSandIslandMexicanHat,
            self.SelwayRiver,
            self.SnakeRiverHellsCanyon,
            self.YampaDeerlodgePark,
        ]

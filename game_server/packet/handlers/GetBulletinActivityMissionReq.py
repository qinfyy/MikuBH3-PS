import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetBulletinActivityMissionReq,
    GetBulletinActivityMissionRsp,
    BulletinMissionGroup,
    PanelMissionData,
    PanelMissionDataPanelMissionCycleData
)

async def handle(session: Session, msg: GetBulletinActivityMissionReq) -> betterproto.Message:
    return GetBulletinActivityMissionRsp(
        retcode=0,
        mission_group_list=[
            BulletinMissionGroup(
                activity_id=5931
            ),
            BulletinMissionGroup(
                activity_id=5938,
                mission_list=[
                    PanelMissionData(
                        mission_id=115679,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729828800,
                                cycle_id=20006997,
                                end_time=1880308800
                            )
                        ]
                    )
                ]
            ),
            BulletinMissionGroup(
                activity_id=5941,
                mission_list=[
                    PanelMissionData(
                        mission_id=687511,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729828800,
                                cycle_id=20007074,
                                end_time=1880308800
                            )
                        ]
                    )
                ]
            ),
            BulletinMissionGroup(
                activity_id=5943,
                mission_list=[
                    PanelMissionData(
                        mission_id=687521,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729828800,
                                cycle_id=20007081,
                                end_time=1880308800
                            )
                        ]
                    )
                ]
            ),
            BulletinMissionGroup(
                activity_id=5944,
                mission_list=[
                    PanelMissionData(
                        mission_id=687530,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007089,
                                end_time=1880308800
                            )
                        ]
                    )
                ]
            ),
            BulletinMissionGroup(
                activity_id=5949,
                mission_list=[
                    PanelMissionData(
                        mission_id=687546,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007106,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687549,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007109,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687566,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007126,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687563,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007123,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687564,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007124,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687565,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007125,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687562,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007122,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687554,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007114,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687555,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007115,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687567,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007127,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687550,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007110,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687551,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007111,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687552,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007112,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687553,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007113,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687560,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007120,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687561,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007121,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687545,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007105,
                                end_time=1880308800
                            )
                        ]
                    )
                ]
            ),
            BulletinMissionGroup(
                activity_id=5952
            ),
            BulletinMissionGroup(
                activity_id=5953,
                mission_list=[
                    PanelMissionData(
                        mission_id=687608,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007187,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687620,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007141,
                                end_time=1880308800
                            )
                        ]
                    ),
                    PanelMissionData(
                        mission_id=687716,
                        cycle_list=[
                            PanelMissionDataPanelMissionCycleData(
                                begin_time=1729108800,
                                cycle_id=20007143,
                                end_time=1880308800
                            )
                        ]
                    )
                ]
            ),
            BulletinMissionGroup(
                activity_id=5959
            ),
            BulletinMissionGroup(
                activity_id=5962
            ),
            BulletinMissionGroup(
                activity_id=5963
            ),
            BulletinMissionGroup(
                activity_id=5964
            )
        ]
    )

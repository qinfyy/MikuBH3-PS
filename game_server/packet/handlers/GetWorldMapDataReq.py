import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetWorldMapDataReq,
    GetWorldMapDataRsp,
    WorldMapData
)

async def handle(session: Session, msg: GetWorldMapDataReq) -> betterproto.Message:
    return GetWorldMapDataRsp(
        retcode=0,
        world_map_list=[
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=1,
                world_map_id=1
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=2,
                world_map_id=2
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                high_light_max_level=30,
                high_light_min_level=25,
                id=3,
                world_map_id=3
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=5,
                weight=1,
                world_map_id=5
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                high_light_max_level=88,
                high_light_min_level=15,
                id=6,
                weight=1,
                world_map_id=6
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                high_light_max_level=40,
                high_light_min_level=30,
                id=7,
                weight=1,
                world_map_id=7
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=8,
                weight=1,
                world_map_id=8
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=9,
                weight=1,
                world_map_id=9
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=10,
                weight=1,
                world_map_id=10
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=11,
                weight=1,
                world_map_id=11
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=49,
                weight=1,
                world_map_id=12
            ),
            WorldMapData(
                advance_time=1563069600,
                begin_time=1563069600,
                end_time=2060107199,
                high_light_max_level=99,
                high_light_min_level=20,
                id=121,
                weight=205,
                world_map_id=2107
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                high_light_max_level=99,
                high_light_min_level=50,
                id=286,
                weight=1,
                world_map_id=18
            ),
            WorldMapData(
                advance_time=1611712800,
                begin_time=1611712800,
                end_time=2060107199,
                high_light_max_level=88,
                high_light_min_level=15,
                id=307,
                weight=1,
                world_map_id=2221
            ),
            WorldMapData(
                advance_time=1705716000,
                begin_time=1705716000,
                end_time=2060107199,
                id=1004,
                weight=1,
                world_map_id=1004
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                id=445,
                weight=1000,
                world_map_id=2313
            ),
            WorldMapData(
                advance_time=1300046400,
                begin_time=1300046400,
                end_time=2060107199,
                high_light_max_level=30,
                high_light_min_level=25,
                id=451,
                world_map_id=19
            ),
            WorldMapData(
                advance_time=1730080800,
                begin_time=1730080800,
                end_time=1880308800,
                id=452,
                weight=1301,
                world_map_id=2317
            ),
            WorldMapData(
                advance_time=1729108800,
                begin_time=1729108800,
                end_time=1880308800,
                id=458,
                weight=122,
                world_map_id=2320
            )
        ]
    )

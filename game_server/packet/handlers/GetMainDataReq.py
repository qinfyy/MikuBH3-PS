import betterproto
from game_server.net.session import Session
from lib.proto import GetMainDataReq,GetMainDataRsp,WarshipAvatarData,ChatworldActivityInfo,WarshipThemeData
from game_server.utils import get_unix_in_seconds

async def handle(session: Session, msg: GetMainDataReq) -> betterproto.Message:
    return GetMainDataRsp(
        retcode=0,
        assistant_avatar_id=session.player.assistant_avatar_id,
        birthday=session.player.birth_date,
        nickname=session.player.name,
        level=session.player.level,
        exp=session.player.exp,
        free_hcoin=0,
        hcoin=session.player.hcoin,
        custom_head_id=session.player.head_photo,
        scoin=0,
        is_all=True,
        register_time=get_unix_in_seconds(),
        pay_hcoin=0,
        warship_avatar=WarshipAvatarData(
            warship_first_avatar_id=session.player.warship_avatar.warship_first_avatar_id,
            warship_second_avatar_id=session.player.warship_avatar.warship_second_avatar_id
        ),
        self_desc=session.player.signature,
        use_frame_id=session.player.head_frame,
        on_phone_pendant_id=350005,
        stamina=session.player.stamina,
        stamina_recover_config_time=360,
        stamina_recover_left_time=360,
        equipment_size_limit=1000,
        open_panel_activity_list=[2],
        chatworld_activity_info=ChatworldActivityInfo(
            is_has_npc_red_envelope=False,
            treasure_schedule_id=0
        ),
        is_allow_cost_senior_equip_on_cur_device=True,
        type_list=[2, 3, 4, 5, 6, 7, 8, 9, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39],
        level_lock_id=1,
        mcoin=100000,
        month_recharge_price=0,
        warship_theme=WarshipThemeData(
            warship_id=session.player.warship_id
        ),
        total_login_days=1,
        next_evaluate_time=0,
        on_medal_id=0,
        today_recharge_price=0
    )

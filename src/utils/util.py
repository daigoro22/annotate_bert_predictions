import logging
import sys

def setup_logger(name):
    """Logger をセットアップする関数.
    Args:
        name (str): Logger の名前空間. __name__ を指定する.
    Returns:
        logger (logging.Logger): セットアップした Logger
    """
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler with a INFO log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # add the handlers to the logger
    logger.addHandler(ch)
    return logger

_dict_class = {
    'その他':('一致',),
    '単語':('同義・類義','上位・下位','含意・前提','全体・部分'),
    'フレーズ':('同義・類義','上位・下位','含意・前提','全体・部分','品詞の変換','共参照・照応'),
    '文構造':('語順入れ替え','態の変化','修飾句削除','主辞削除','並列・従属節','集合・リスト','同格','関係節'),
    '推論':('時間の推論','空間の推論','数の推論','暗黙の関係','その他の推論')
}
_dict_class = {k:[f'{k}:{vl}' for vl in v] for k,v in _dict_class.items()}
list_class = sum(_dict_class.values(),[])
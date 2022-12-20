__chess__ = {
    #black
    'b': '卒',
    'p': '砲',
    'c': '車',
    'm': '馬',
    'x': '象',
    's': '士',
    'k': '將',
    #RED
    'B': '兵',
    'P': '炮',
    'C': '俥',
    'M': '傌',
    'X': '相',
    'S': '仕',
    'K': '帥'
}

__board_line__ = ['┏━━━┯━━━┯━━━┯━━━┯━━━┯━━━┯━━━┯━━━┓', 
                  '┃   │   │   │ ╲ │ ╱ │   │   │   ┃',
                  '┠───┼───┼───┼───┼───┼───┼───┼───┨',
                  '┃   │   │   │ ╱ │ ╲ │   │   │   ┃',
                  '┠───╬───┼───┼───┼───┼───┼───╬───┨',
                  '┃   │   │   │   │   │   │   │   ┃',
                  '╠───┼───╬───┼───╬───┼───╬───┼───╣',
                  '┃   │   │   │   │   │   │   │   ┃',
                  '┠═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══┨',
                  '┃       楚河         漢界       ┃',
                  '┠═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══┨',
                  '┃   │   │   │   │   │   │   │   ┃',
                  '╠───┼───╬───┼───╬───┼───╬───┼───╣',
                  '┃   │   │   │   │   │   │   │   ┃',
                  '┠───╬───┼───┼───┼───┼───┼───╬───┨',
                  '┃   │   │   │ ╲ │ ╱ │   │   │   ┃',
                  '┠───┼───┼───┼───┼───┼───┼───┼───┨',
                  '┃   │   │   │ ╱ │ ╲ │   │   │   ┃',
                  '┗━━━┷━━━┷━━━┷━━━┷━━━┷━━━┷━━━┷━━━┛']

__board_data__ = [['c', 'm', 'x', 's', 'k', 's', 'x', 'm', 'c'],
                  ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                  ['0', 'p', '0', '0', '0', '0', '0', 'p', '0'],
                  ['b', '0', 'b', '0', 'b', '0', 'b', '0', 'b'],
                  ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                  ['B', '0', 'B', '0', 'B', '0', 'B', '0', 'B'],
                  ['0', 'P', '0', '0', '0', '0', '0', 'P', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                  ['C', 'M', 'X', 'S', 'K', 'S', 'X', 'M', 'C']]
  
def getDefaultChessDictionary():
    return __chess__

def getDefaultBoardData():
    return __board_data__

def getDefaultBoardLine():
    return __board_line__
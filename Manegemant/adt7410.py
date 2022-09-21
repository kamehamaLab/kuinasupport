import smbus

bus = smbus.SMBus(1)
address_adt7410 = 0x48
register_adt7410 = 0x00
configration_adt7410 = 0x03

# 13bitに設定して読み出し
bus.write_word_data(address_adt7410, configration_adt7410, 0x00)
word_data = bus.read_word_data(address_adt7410, register_adt7410)

# ２バイトの入れ替え
data = (word_data & 0xff00) >> 8 | (word_data & 0xff) << 8

# 3ビットの右シフト
data = data >> 3

# 16で割って温度に
print(data/16.)

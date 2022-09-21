import smbus

bus = smbus.SMBus(1)
address_adt7410 = 0x48
register_adt7410 = 0x00
configration_adt7410 = 0x03

bus.write_word_data(address_adt7410, configration_adt7410, 0x00)
word_data = bus.read_word_data(address_adt7410, register_adt7410)
data = (word_data & 0xff00) >> 8 | (word_data & 0xff) << 8
data = data >> 3
print(data/16.)

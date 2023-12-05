class StorageDevice:
    def __init__(self, capacity, interface):
        self.capacity = capacity  
        self.interface = interface  
    def get_info(self):
        return f"Устройство: {self.__class__.__name__}, Объем: {self.capacity} ГБ, Интерфейс: {self.interface}"

class HardDisk(StorageDevice):
    def __init__(self, capacity, interface, rpm):
        super().__init__(capacity, interface)
        self.rpm = rpm  
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Скорость вращения: {self.rpm} об/мин"

class FlashDrive(StorageDevice):
    def __init__(self, capacity, interface, usb_version):
        super().__init__(capacity, interface)
        self.usb_version = usb_version  
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Версия USB: {self.usb_version}"

hdd = HardDisk(1000, "SATA", 7200)
usb_drive = FlashDrive(64, "USB 3.0", "USB 3.0")

print(hdd.get_info())  
print(usb_drive.get_info())  


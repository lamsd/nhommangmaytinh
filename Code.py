import numpy as np
import matplotlib.pyplot as plt

def noma_iot_simulation(snr_db_range):
    """ Mô phỏng hệ thống IoT sử dụng NOMA với Energy Harvesting """
    snr_linear = 10 ** (np.array(snr_db_range) / 10)  # Chuyển SNR từ dB sang giá trị tuyến tính
    ber_sensor1 = []  # Cảm biến 1 (mạnh hơn)
    ber_sensor2 = []  # Cảm biến 2 (yếu hơn)
    
    for snr in snr_linear:
        noise_power = 1 / snr  # Công suất nhiễu
        sensor1_power = 0.7  # Công suất cảm biến 1
        sensor2_power = 0.3  # Công suất cảm biến 2
        
        # Tạo tín hiệu nhị phân cho cảm biến IoT
        sensor1_signal = np.random.randint(0, 2, 10000)
        sensor2_signal = np.random.randint(0, 2, 10000)
        
        # Điều chế BPSK (-1 hoặc +1)
        mod_sensor1 = 2 * sensor1_signal - 1
        mod_sensor2 = 2 * sensor2_signal - 1
        
        # Tín hiệu NOMA tổng hợp
        noma_signal = np.sqrt(sensor1_power) * mod_sensor1 + np.sqrt(sensor2_power) * mod_sensor2
        
        # Thêm nhiễu Gaussian vào tín hiệu truyền
        noise = np.sqrt(noise_power) * np.random.randn(len(noma_signal))
        received_signal = noma_signal + noise
        
        # Giải mã SIC (Successive Interference Cancellation)
        decoded_sensor1 = np.sign(received_signal - np.sqrt(sensor2_power) * mod_sensor2)
        decoded_sensor2 = np.sign(received_signal / np.sqrt(sensor2_power))
        
        # Tính BER (Bit Error Rate - Tỷ lệ lỗi bit)
        ber_sensor1.append(np.mean(decoded_sensor1 != mod_sensor1))
        ber_sensor2.append(np.mean(decoded_sensor2 != mod_sensor2))
    
    return ber_sensor1, ber_sensor2

def energy_harvesting_iot(snr_db_range):
    """ Mô phỏng năng lượng thu được của cảm biến IoT từ môi trường """
    snr_linear = 10 ** (np.array(snr_db_range) / 10)
    harvested_energy = []
    efficiency_factor = 0.5  # Hiệu suất thu năng lượng (50%)
    
    for snr in snr_linear:
        received_power = 1 / snr  # Công suất nhận được từ tín hiệu
        harvested_energy.append(efficiency_factor * received_power)  # Năng lượng thu được
    
    return harvested_energy

def noma_its_simulation(snr_db_range):
    """ Mô phỏng hệ thống giao thông thông minh (ITS) sử dụng NOMA """
    snr_linear = 10 ** (np.array(snr_db_range) / 10)
    ber_vehicle1 = []  # Xe 1 (tín hiệu mạnh hơn)
    ber_vehicle2 = []  # Xe 2 (tín hiệu yếu hơn)
    
    for snr in snr_linear:
        noise_power = 1 / snr
        vehicle1_power = 0.6  # Công suất của xe 1
        vehicle2_power = 0.4  # Công suất của xe 2
        
        # Tạo tín hiệu nhị phân
        vehicle1_signal = np.random.randint(0, 2, 10000)
        vehicle2_signal = np.random.randint(0, 2, 10000)
        
        # Điều chế BPSK
        mod_vehicle1 = 2 * vehicle1_signal - 1
        mod_vehicle2 = 2 * vehicle2_signal - 1
        
        # Ghép tín hiệu NOMA
        noma_signal = np.sqrt(vehicle1_power) * mod_vehicle1 + np.sqrt(vehicle2_power) * mod_vehicle2
        
        # Thêm nhiễu Gaussian
        noise = np.sqrt(noise_power) * np.random.randn(len(noma_signal))
        received_signal = noma_signal + noise
        
        # Giải mã SIC
        decoded_vehicle1 = np.sign(received_signal - np.sqrt(vehicle2_power) * mod_vehicle2)
        decoded_vehicle2 = np.sign(received_signal / np.sqrt(vehicle2_power))
        
        # Tính BER
        ber_vehicle1.append(np.mean(decoded_vehicle1 != mod_vehicle1))
        ber_vehicle2.append(np.mean(decoded_vehicle2 != mod_vehicle2))
    
    return ber_vehicle1, ber_vehicle2

def noma_nr_v2x_simulation(snr_db_range):
    """ Mô phỏng hệ thống NR V2X sử dụng NOMA """
    snr_linear = 10 ** (np.array(snr_db_range) / 10)
    ber_vehicle1 = []  # Xe 1 (tín hiệu mạnh hơn)
    ber_vehicle2 = []  # Xe 2 (tín hiệu yếu hơn)
    
    for snr in snr_linear:
        noise_power = 1 / snr
        vehicle1_power = 0.7  # Công suất của xe 1
        vehicle2_power = 0.3  # Công suất của xe 2
        
        # Tạo tín hiệu nhị phân
        vehicle1_signal = np.random.randint(0, 2, 10000)
        vehicle2_signal = np.random.randint(0, 2, 10000)
        
        # Điều chế BPSK
        mod_vehicle1 = 2 * vehicle1_signal - 1
        mod_vehicle2 = 2 * vehicle2_signal - 1
        
        # Ghép tín hiệu NOMA
        noma_signal = np.sqrt(vehicle1_power) * mod_vehicle1 + np.sqrt(vehicle2_power) * mod_vehicle2
        
        # Thêm nhiễu Gaussian
        noise = np.sqrt(noise_power) * np.random.randn(len(noma_signal))
        received_signal = noma_signal + noise
        
        # Giải mã SIC
        decoded_vehicle1 = np.sign(received_signal - np.sqrt(vehicle2_power) * mod_vehicle2)
        decoded_vehicle2 = np.sign(received_signal / np.sqrt(vehicle2_power))
        
        # Tính BER
        ber_vehicle1.append(np.mean(decoded_vehicle1 != mod_vehicle1))
        ber_vehicle2.append(np.mean(decoded_vehicle2 != mod_vehicle2))
    
    return ber_vehicle1, ber_vehicle2

# Phạm vi SNR (dB)
snr_db_range = np.arange(0, 20, 2)

# Chạy mô phỏng hệ thống IoT sử dụng NOMA
ber_sensor1, ber_sensor2 = noma_iot_simulation(snr_db_range)

# Chạy mô phỏng hệ thống giao thông thông minh sử dụng NOMA
ber_vehicle1, ber_vehicle2 = noma_its_simulation(snr_db_range)

# Chạy mô phỏng năng lượng thu được từ môi trường
harvested_energy = energy_harvesting_iot(snr_db_range)

# Chạy mô phỏng hệ thống NR V2X sử dụng NOMA
ber_vehicle1, ber_vehicle2 = noma_nr_v2x_simulation(snr_db_range)

# Vẽ biểu đồ BER của hệ thống IoT sử dụng NOMA
plt.figure(num="Biểu đồ BER của hệ thống IoT sử dụng NOMA")
plt.semilogy(snr_db_range, ber_sensor1, 'o-', label='Cảm biến 1 (Mạnh)')
plt.semilogy(snr_db_range, ber_sensor2, 's-', label='Cảm biến 2 (Yếu)')
plt.xlabel('SNR (dB)')
plt.ylabel('BER (Tỷ lệ lỗi bit)')
plt.title('Biểu đồ BER của hệ thống IoT sử dụng NOMA')
plt.legend()
plt.grid(True)
plt.show()

# Vẽ biểu đồ BER của hệ thống giao thông thông minh sử dụng NOMA
plt.figure(num="Biểu đồ BER của hệ thống giao thông thông minh sử dụng NOMA")
plt.semilogy(snr_db_range, ber_vehicle1, 'o-', label='Xe 1 (Mạnh)')
plt.semilogy(snr_db_range, ber_vehicle2, 's-', label='Xe 2 (Yếu)')
plt.xlabel('SNR (dB)')
plt.ylabel('BER (Tỷ lệ lỗi bit)')
plt.title('Biểu đồ BER của hệ thống giao thông thông minh sử dụng NOMA')
plt.legend()
plt.grid(True)
plt.show()

# Vẽ biểu đồ năng lượng thu được từ môi trường
plt.figure('Biểu đồ năng lượng thu được của IoT từ môi trường')
plt.plot(snr_db_range, harvested_energy, 'o-', label='Năng lượng thu được')
plt.xlabel('SNR (dB)')
plt.ylabel('Năng lượng thu được (Đơn vị chuẩn hóa)')
plt.title('Biểu đồ năng lượng thu được của IoT từ môi trường')
plt.legend()
plt.grid(True)
plt.show()


# Vẽ biểu đồ BER của hệ thống NR V2X sử dụng NOMA
plt.figure('Biểu đồ BER của hệ thống NR V2X sử dụng NOMA')
plt.semilogy(snr_db_range, ber_vehicle1, 'o-', label='Xe 1 (Mạnh)')
plt.semilogy(snr_db_range, ber_vehicle2, 's-', label='Xe 2 (Yếu)')
plt.xlabel('SNR (dB)')
plt.ylabel('BER (Tỷ lệ lỗi bit)')
plt.title('Biểu đồ BER của hệ thống NR V2X sử dụng NOMA')
plt.legend()
plt.grid(True)
plt.show()
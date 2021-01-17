import streamlit as st
import numpy as np

####Parameters
#Constant (Pi)
Pi                  = np.pi

##Fabrication Parameters
#Baseline Process Node
#Unit: [nm]
Baseline_Process    = 45

##Design Parameters
#Chip Area
#Unit: [mm**2]
Baseline_Chip_Area  = 100

#Logic Area@45nm
#Unit: [umm**2]
Baseline_Area_Add_Int_8bit  = 36
Baseline_Area_Add_Int_16bit = 67
Baseline_Area_Add_Int_32bit = 137
Baseline_Area_Mlt_Int_8bit  = 282
Baseline_Area_Mlt_Int_16bit = 1000
Baseline_Area_Mlt_Int_32bit = 3495

Baseline_Area_Add_Fp_16bit  = 1360
Baseline_Area_Add_Fp_32bit  = 4184
Baseline_Area_Mlt_Fp_16bit  = 1640
Baseline_Area_Mlt_Fp_32bit  = 7700

Baseline_Energy_SRAM_8KiB   = 5.0

#Logic Energy@45nm
#Unit: [pJ]
Baseline_Energy_Add_Int_8bit    = 0.03
Baseline_Energy_Add_Int_16bit   = 0.05
Baseline_Energy_Add_Int_32bit   = 0.1
Baseline_Energy_Mlt_Int_8bit    = 0.2
Baseline_Energy_Mlt_Int_16bit   = 0.75
Baseline_Energy_Mlt_Int_32bit   = 3.1

Baseline_Energy_Add_Fp_16bit    = 0.4
Baseline_Energy_Add_Fp_32bit    = 0.9
Baseline_Energy_Mlt_Fp_16bit    = 1.1
Baseline_Energy_Mlt_Fp_32bit    = 3.7

#SRAM Cell Area@45nm
Baseline_Area_SRAM_Cell         = 0.299

#SRAM Cell Energy@45nm
Baseline_Energy_SRAM_Cell       = 0.00007629394


st.title('Logic Cost Estimation')

#Targetting Process Node
#Unit: [%]
process_node = st.sidebar.slider('Process Node [nm]', 3, 65, Baseline_Process)
st.text('Process Node [nm]          %s' % process_node)

#Scale Factor
scale_factor = float(Baseline_Process) / float(process_node)

##Area [45nm]
#Chip Area
chip_area = st.sidebar.slider('Chip Area [mm**2]', 1, 900, Baseline_Chip_Area)
st.text('Chip Area [mm**2]          %s' % chip_area)


st.subheader('Area for Integer')
#Unit: [um**2]
area_Int_add_08b = int(np.ceil(float(Baseline_Area_Add_Int_8bit) / float(scale_factor)))
st.text('Adder  (8-bit) [um**2]     %s' % area_Int_add_08b)

area_Int_add_16b = int(np.ceil(float(Baseline_Area_Add_Int_16bit) / float(scale_factor)))
st.text('Adder (16-bit) [um**2]     %s' % area_Int_add_16b)

area_Int_add_32b = int(np.ceil(float(Baseline_Area_Add_Int_32bit) / float(scale_factor)))
st.text('Adder (32-bit) [um**2]     %s' % area_Int_add_32b)

area_Int_mlt_08b = int(np.ceil(float(Baseline_Area_Mlt_Int_8bit) / float(scale_factor**2)))
st.text('Multiplier (8-bit) [um**2] %s' % area_Int_mlt_08b)

area_Int_mlt_16b = int(np.ceil(float(Baseline_Area_Mlt_Int_16bit) / float(scale_factor**2)))
st.text('Multiplier (16-bit) [um**2]%s' % area_Int_mlt_16b)

area_Int_mlt_32b = int(np.ceil(float(Baseline_Area_Mlt_Int_32bit) / float(scale_factor**2)))
st.text('Multiplier (32-bit) [um**2]%s' % area_Int_mlt_32b)

##Energy [45nm]
#Unit: [pJ]
st.subheader('Energy Consumption for Interger')
energy_Int_add_08b = float(Baseline_Energy_Add_Int_8bit) / float(scale_factor)
st.text('Adder  (8-bit) [pJ]        %s' % energy_Int_add_08b)

energy_Int_add_16b = float(Baseline_Energy_Add_Int_16bit) / float(scale_factor)
st.text('Adder (16-bit) [pJ]        %s' % energy_Int_add_16b)

energy_Int_add_32b = float(Baseline_Energy_Add_Int_32bit) / float(scale_factor)
st.text('Adder (32-bit) [pJ]        %s' % energy_Int_add_32b)

energy_Int_mlt_08b = float(Baseline_Energy_Mlt_Int_8bit) / float(scale_factor**2)
st.text('Multiplier (8-bit) [pJ]    %s' % energy_Int_mlt_08b)

energy_Int_mlt_16b = float(Baseline_Energy_Mlt_Int_16bit) / float(scale_factor**2)
st.text('Multiplier (16-bit) [pJ]   %s' % energy_Int_mlt_16b)

energy_Int_mlt_32b = float(Baseline_Energy_Mlt_Int_32bit) / float(scale_factor**2)
st.text('Multiplier (32-bit) [pJ]   %s' % energy_Int_mlt_32b)


st.subheader('Area for Floating-Point')
area_Fp_add_16b = int(np.ceil(float(Baseline_Area_Add_Fp_16bit) / float(scale_factor)))
st.text('Adder (16-bit) [um**2]     %s' % area_Fp_add_16b)

area_Fp_add_32b = int(np.ceil(float(Baseline_Area_Add_Fp_32bit) / float(scale_factor)))
st.text('Adder (32-bit) [um**2]     %s' % area_Fp_add_32b)

area_Fp_mlt_16b = int(np.ceil(float(Baseline_Area_Mlt_Fp_16bit) / float(scale_factor**2)))
st.text('Multiplier (16-bit) [um**2]%s' % area_Fp_mlt_16b)

area_Fp_mlt_32b = int(np.ceil(float(Baseline_Area_Mlt_Fp_32bit) / float(scale_factor**2)))
st.text('Multiplier (32-bit) [um**2]%s' % area_Fp_mlt_32b)

st.subheader('Energy Consumption for Floating-Point')
energy_Fp_add_16b = float(Baseline_Energy_Add_Fp_16bit) / float(scale_factor)
st.text('Adder (16-bit) [pJ]        %s' % energy_Fp_add_16b)

energy_Fp_add_32b = float(Baseline_Energy_Add_Fp_32bit) / float(scale_factor)
st.text('Adder (32-bit) [pJ]        %s' % energy_Fp_add_32b)

energy_Fp_mlt_16b = float(Baseline_Energy_Mlt_Fp_16bit) / float(scale_factor**2)
st.text('Multiplier (16-bit) [pJ]   %s' % energy_Fp_mlt_16b)

energy_Fp_mlt_32b = float(Baseline_Energy_Mlt_Fp_32bit) / float(scale_factor**2)
st.text('Multiplier (32-bit) [pJ]   %s' % energy_Fp_mlt_32b)

st.subheader('Area')
effective_area_rate = st.sidebar.slider('Effective Area [mm**2]', 0.0, 100.0, 80.0)
effective_chip_area = chip_area * effective_area_rate / 100.0
st.text('Effective Area [mm**2]     %s' % effective_chip_area)

effective_chip_area_um = effective_chip_area * 1000000

##Number of Integer Logic Circuits
st.sidebar.subheader('Number of Integer Units')
max_num_Int_add_08b = int(np.floor(float(effective_chip_area_um) / float(area_Int_add_08b)))
num_Int_add_08b = st.sidebar.slider('Number of Adders (8-bit)', 0, max_num_Int_add_08b, 0)

max_num_Int_add_16b = int(np.floor(float(effective_chip_area_um) / float(area_Int_add_16b)))
num_Int_add_16b = st.sidebar.slider('Number of Adders (16-bit)', 0, max_num_Int_add_16b, 0)

max_num_Int_add_32b = int(np.floor(float(effective_chip_area_um) / float(area_Int_add_32b)))
num_Int_add_32b = st.sidebar.slider('Number of Adders (32-bit)', 0, max_num_Int_add_32b, 0)

max_num_Int_mlt_08b = int(np.floor(float(effective_chip_area_um) / float(area_Int_mlt_08b)))
num_Int_mlt_08b = st.sidebar.slider('Number of Multipliers (8-bit)', 0, max_num_Int_mlt_08b, 0)

max_num_Int_mlt_16b = int(np.floor(float(effective_chip_area_um) / float(area_Int_mlt_16b)))
num_Int_mlt_16b = st.sidebar.slider('Number of Multipliers (16-bit)', 0, max_num_Int_mlt_16b, 0)

max_num_Int_mlt_32b = int(np.floor(float(effective_chip_area_um) / float(area_Int_mlt_32b)))
num_Int_mlt_32b = st.sidebar.slider('Number of Multipliers (32-bit)', 0, max_num_Int_mlt_32b, 0)

##Number of Floating-Point Logic Circuits
st.sidebar.subheader('Number of Floating-point Units')
max_num_Fp_add_16b = int(np.floor(float(effective_chip_area_um) / float(area_Fp_add_16b)))
num_Fp_add_16b = st.sidebar.slider('Number of Adders (16-bit)', 0, max_num_Fp_add_16b, 0)

max_num_Fp_add_32b = int(np.floor(float(effective_chip_area_um) / float(area_Fp_add_32b)))
num_Fp_add_32b = st.sidebar.slider('Number of Adders (32-bit)', 0, max_num_Fp_add_32b, 0)

max_num_Fp_mlt_16b = int(np.floor(float(effective_chip_area_um) / float(area_Fp_mlt_16b)))
num_Fp_mlt_16b = st.sidebar.slider('Number of Multipliers (16-bit)', 0, max_num_Fp_mlt_16b, 0)

max_num_Fp_mlt_32b = int(np.floor(float(effective_chip_area_um) / float(area_Fp_mlt_32b)))
num_Fp_mlt_32b = st.sidebar.slider('Number of Multipliers (32-bit)', 0, max_num_Fp_mlt_32b, 0)

##Number of MAC Logic Circuits
st.sidebar.subheader('Number of Integer MACs')
max_num_mac_Int_08m32a = int(np.floor(float(effective_chip_area_um) / float(area_Int_mlt_08b + area_Int_add_32b)))
num_mac_Int_08m32a = st.sidebar.slider('Int 8b Mlt and 32b Add', 0, max_num_mac_Int_08m32a, 0)

max_num_mac_Int_16m32a = int(np.floor(float(effective_chip_area_um) / float(area_Int_mlt_16b + area_Int_add_32b)))
num_mac_Int_16m32a = st.sidebar.slider('Int 16b Mlt and 32b Add', 0, max_num_mac_Int_16m32a, 0)

max_num_mac_Int_32m32a = int(np.floor(float(effective_chip_area_um) / float(area_Int_mlt_32b + area_Int_add_32b)))
num_mac_Int_32m32a = st.sidebar.slider('Int 32b Mlt and 32b Add', 0, max_num_mac_Int_32m32a, 0)

st.sidebar.subheader('Number of Floating-Point MACs')
max_num_mac_Fp_16m16a = int(np.floor(float(effective_chip_area_um) / float(area_Fp_mlt_16b + area_Fp_add_16b)))
num_mac_Fp_16m16a = st.sidebar.slider('Float 16b Mlt and 16b Add', 0, max_num_mac_Fp_16m16a, 0)

max_num_mac_Fp_16m32a = int(np.floor(float(effective_chip_area_um) / float(area_Fp_mlt_16b + area_Fp_add_32b)))
num_mac_Fp_16m32a = st.sidebar.slider('Float 16b Mlt and 32b Add', 0, max_num_mac_Fp_16m32a, 0)

max_num_mac_Fp_32m32a = int(np.floor(float(effective_chip_area_um) / float(area_Fp_mlt_32b + area_Fp_add_32b)))
num_mac_Fp_32m32a = st.sidebar.slider('Float 32b Mlt and 32b Add', 0, max_num_mac_Fp_32m32a, 0)


st.sidebar.subheader('On-Chip SRAM')
st.subheader('On-Chip SRAM')
size_sram = st.sidebar.slider('SRAM Size [KiB]', 0, 256, 0)
st.text('SRAM Size [KiB]            %s' % size_sram)

area_sram = size_sram * 8 * 1024
st.text('SRAM Area [um**2]          %s' % area_sram)

if area_sram > 0.0:
    max_num_sram = int(np.floor(float(effective_chip_area_um) / float(area_sram)))
else:
    max_num_sram = 0
num_sram = st.sidebar.slider('Number of SRAMs', 0, max_num_sram+1, max_num_sram)
st.text('Number of SRAMs            %s' % num_sram)

st.subheader('Total Area for Integer Unit')
total_area_Int_add_08b = area_Int_add_08b * num_Int_add_08b
st.text('Adder  (8-bit) [um**2]     %s' % total_area_Int_add_08b)

total_area_Int_add_16b = area_Int_add_16b * num_Int_add_16b
st.text('Adder (16-bit) [um**2]     %s' % total_area_Int_add_16b)

total_area_Int_add_32b = area_Int_add_32b * num_Int_add_32b
st.text('Adder (32-bit) [um**2]     %s' % total_area_Int_add_32b)

total_area_Int_mlt_08b = area_Int_mlt_08b * num_Int_mlt_08b
st.text('Multiplier  (8-bit) [um**2]%s' % total_area_Int_mlt_08b)

total_area_Int_mlt_16b = area_Int_mlt_16b * num_Int_mlt_16b
st.text('Multiplier (16-bit) [um**2]%s' % total_area_Int_mlt_16b)

total_area_Int_mlt_32b = area_Int_mlt_32b * num_Int_mlt_32b
st.text('Multiplier (32-bit) [um**2]%s' % total_area_Int_mlt_32b)

st.subheader('Total Area for Floating-Point Unit')
total_area_Fp_add_16b = area_Fp_add_16b * num_Fp_add_16b
st.text('Adder (16-bit) [um**2]     %s' % total_area_Fp_add_16b)

total_area_Fp_add_32b = area_Fp_add_32b * num_Fp_add_32b
st.text('Adder (32-bit) [um**2]     %s' % total_area_Fp_add_32b)

total_area_Fp_mlt_16b = area_Fp_mlt_16b * num_Fp_mlt_16b
st.text('Multiplier (16-bit) [um**2]%s' % total_area_Fp_mlt_16b)

total_area_Fp_mlt_32b = area_Fp_mlt_32b * num_Fp_mlt_32b
st.text('Multiplier (32-bit) [um**2]%s' % total_area_Fp_mlt_32b)

st.subheader('Total Area for Integer MACs w/o SRAMs')
total_area_Int_mac_08m32a = float(num_mac_Int_08m32a) * float(area_Int_add_08b + area_Int_add_32b) / 1000000.0
st.text(' 8b Mlt and 32b Add [mm**2]        %s' % total_area_Int_mac_08m32a)
area_ratio_Int_mac_08m32a = (total_area_Int_mac_08m32a * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Int_mac_08m32a)

total_area_Int_mac_16m32a = float(num_mac_Int_16m32a) * float(area_Int_add_16b + area_Int_add_32b) / 1000000.0
st.text('16b Mlt and 32b Add [mm**2]        %s' % total_area_Int_mac_16m32a)
area_ratio_Int_mac_16m32a = (total_area_Int_mac_16m32a * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Int_mac_16m32a)

total_area_Int_mac_32m32a = float(num_mac_Int_32m32a) * float(area_Int_add_32b + area_Int_add_32b) / 1000000.0
st.text('32b Mlt and 32b Add [mm**2]        %s' % total_area_Int_mac_32m32a)
area_ratio_Int_mac_32m32a = (total_area_Int_mac_32m32a * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Int_mac_32m32a)

st.subheader('Total Area for Integer MACs w/ SRAMs')
if num_mac_Int_08m32a <= 0.0:
    total_area_Int_mac_08m32a_sram = 0.0
else:
    total_area_Int_mac_08m32a_sram = ((float(num_mac_Int_08m32a) * float(area_Int_add_08b + area_Int_add_32b)) + float(num_sram * float(area_sram))) / 1000000.0
st.text(' 8b Mlt and 32b Add [um**2]        %s' % total_area_Int_mac_08m32a_sram)
area_ratio_Int_mac_08m32a_sram = (total_area_Int_mac_08m32a_sram * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Int_mac_08m32a_sram)

if num_mac_Int_16m32a <= 0.0:
    total_area_Int_mac_16m32a_sram = 0.0
else:
    total_area_Int_mac_16m32a_sram = ((float(num_mac_Int_16m32a) * float(area_Int_add_16b + area_Int_add_32b)) + float(num_sram * float(area_sram))) / 1000000.0
st.text('16b Mlt and 32b Add [um**2]        %s' % total_area_Int_mac_16m32a_sram)
area_ratio_Int_mac_16m32a_sram = (total_area_Int_mac_16m32a_sram * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Int_mac_16m32a_sram)

if num_mac_Int_32m32a <= 0.0:
    total_area_Int_mac_32m32a_sram = 0.0
else:
    total_area_Int_mac_32m32a_sram = ((float(num_mac_Int_32m32a) * float(area_Int_add_32b + area_Int_add_32b)) + float(num_sram * float(area_sram))) / 1000000.0
st.text('32b Mlt and 32b Add [um**2]        %s' % total_area_Int_mac_32m32a_sram)
area_ratio_Int_mac_32m32a_sram = (total_area_Int_mac_32m32a_sram * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Int_mac_32m32a_sram)


st.subheader('Total Area for Floating-Point MACs w/o SRAMs')
total_area_Fp_mac_16m32a = (float(num_mac_Fp_16m32a) * float(area_Fp_add_16b + area_Fp_add_32b)) / 1000000.0
st.text('16b Mlt and 32b Add [mm**2]        %s' % total_area_Fp_mac_16m32a)
area_ratio_Fp_mac_16m32a = (total_area_Fp_mac_16m32a * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Fp_mac_16m32a)

total_area_Fp_mac_32m32a = (float(num_mac_Fp_32m32a) * float(area_Fp_add_32b + area_Fp_add_32b)) / 1000000.0
st.text('32b Mlt and 32b Add [mm**2]        %s' % total_area_Fp_mac_32m32a)
area_ratio_Fp_mac_32m32a = (total_area_Fp_mac_32m32a * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Fp_mac_32m32a)


st.subheader('Total Area for Floating-Point MACs w/ SRAMs')
total_area_Fp_mac_16m32a_sram = ((float(num_mac_Fp_16m32a) * float(area_Fp_add_16b + area_Fp_add_32b)) + float(num_sram * float(area_sram))) / 1000000.0
st.text('16b Mlt and 32b Add [mm**2]        %s' % total_area_Fp_mac_16m32a_sram)
area_ratio_Fp_mac_16m32a_sram = (total_area_Fp_mac_16m32a_sram * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Fp_mac_16m32a_sram)

total_area_Fp_mac_32m32a_sram = ((float(num_mac_Fp_32m32a) * float(area_Fp_add_32b + area_Fp_add_32b)) + float(num_sram * float(area_sram))) / 1000000.0
st.text('32b Mlt and 32b Add [mm**2]        %s' % total_area_Fp_mac_32m32a_sram)
area_ratio_Fp_mac_32m32a_sram = (total_area_Fp_mac_32m32a_sram * 100.0 / effective_chip_area)
st.text('Percentile in Effective Chip Area  %s' % area_ratio_Fp_mac_32m32a_sram)

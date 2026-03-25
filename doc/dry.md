# Maersk OneEdge Dry – Sensor and Event Findings

## 1. Temperature Monitoring

### 1.1 Scheduled Temperature Data
- **Sampling Interval**: Every 5 minutes (may be longer due to power constraints).
- **Reported Values**:
  - Average temperature
  - Minimum temperature
  - Maximum temperature
  - Current temperature
- **Data Type**: Integer
- **Accuracy**: ±0.5 °C (due to integer data representation)
- **Unit**: Celsius (°C)
- **Sensors**: V1 and V2
- **Reset Behavior**: Values reset after each CU read command

### 1.2 Extreme Temperature Change Event (V2 Only)
- **Trigger Condition**: Rapid temperature change exceeding +60 °C
- **Detection Mechanism**:
  - Dual-threshold interrupt setup
  - Timer-based rate calculation
  - Fallback mechanism if second threshold is not triggered
- **Reported Data**:
  - Latest temperature value
  - Temperature delta (fixed-point integer, scale factor 10)
  - Time duration between changes
- **Unit**: Celsius and Celsius per minute

### 1.3 High / Low Temperature Event (V2 Only)
- **Thresholds**:
  - Low alert: -20 °C
  - High alert: +50 °C
- **Event Logic**: Event triggered on threshold breach, and again once cleared
- **Reported Data**: Latest temperature value
- **Accuracy**: ±0.5 °C
- **Unit**: Celsius (°C)

## 2. Humidity Monitoring

### 2.1 Scheduled Humidity Data
- **Sampling Interval**: Every 5 minutes
- **Reported Values**:
  - Average humidity
  - Minimum humidity
  - Maximum humidity
  - Current humidity
- **Data Type**: Unsigned integer
- **Accuracy**: ±0.5 %RH
- **Unit**: Relative Humidity (%)
- **Sensors**: V1 and V2
- **Reset Behavior**: Values reset after each CU read command
- **Event Support**: No event-triggered logic defined

## 3. Light Level Monitoring (V2 Only)

- **Sensor**: Ambient Light Sensor (ALS)
- **Access Method**: Read on demand by CU
- **Application**: Supports door open/close detection
- **Data Type**: Unsigned integer
- **Unit**: Lux
- **Accuracy**: Not defined
- **Event Support**: Not a standalone event

## 4. Door Open/Close Detection

### 4.1 Sensor V1 (Treon Asset Sensor)
- **Detection Method**: ALS-based thresholding
- **Logic**:
  - Door open: ALS value > 50
  - Door closed: ALS value < 40
- **Limitations**:
  - Reduced reliability in low-light conditions
  - Thresholds configurable via FOTA

### 4.2 Sensor V2
- **Detection Method**: Inductive sensor with accelerometer trigger
- **Sampling**: 60-second intervals or on motion detection
- **Event**: Sent on state change
- **Data**:
  - Door state (boolean)
  - Unit: Open/Close

## 5. Stuffing Level Detection (V2 Only)

- **Trigger**: After door closes and a 30-minute timeout expires
- **Sensors**:
  - Radar (radio frequency-based)
  - TOF (optical Time-of-Flight)
- **Radar Output**:
  - Up to 9 distance-strength reflection pairs
- **TOF Output**:
  - 8x8 matrix of depth values (64 points)
  - Maximum range: 4 meters
- **Data Handling**:
  - Raw data is sent to the CU and cloud
  - Initial processing occurs in the cloud
  - Future goal: sensor-side computation

## 6. Lift Detection (CU Only)

- **Trigger**: Vertical movement detected via accelerometer
- **Measurement**: Relative pressure change from barometer
- **Barometer Accuracy**: ±0.2 hPa
- **Reported Data**:
  - Ascend (vertical meters)
  - Descend (vertical meters)
  - Duration (seconds)
  - Timestamp
- **Unit**: Meters, seconds

## 7. Device Diagnostics

- **Reported Metrics**:
  - Battery voltage
  - Connectivity quality between CU and sensors
- **Purpose**: Monitor device health
- **Event Structure**: Not separately named but included in diagnostics data

## 8. Sensor Data Delivery

- **Format**: CBOR blob
- **Standard**: dry-sensor-if.cddl
- **Workflow**:
  - Sensor packages data as CBOR
  - CU receives and transmits to the cloud
  - CU buffers data if offline
  - Cloud parses CBOR data

## 9. Cloud-Based Calculations

- **Dew Point**: Calculated from temperature and humidity values
- **Stuffing Level**: Calculated using TOF and radar data in cloud
- **Future Goal**: Offload processing to V2 sensor

## 10. Sensor Overview

| Component                 | Role                                                                 |
|---------------------------|----------------------------------------------------------------------|
| CU (Connectivity Unit)    | MQTT communication, sensor polling, data buffering, lift event       |
| In-container Sensor V1    | Basic temperature/humidity monitoring, ALS-based door detection      |
| In-container Sensor V2    | Advanced sensing: temperature, humidity, door (inductive), light, stuffing level |

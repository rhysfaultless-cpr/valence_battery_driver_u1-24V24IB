# valence_battery_driver_u1-24V24IB

## Hardware

| Item Description                          | Manufacturer       | Item Number                                                                   | Quantity |
| :---------------------------------------- | :----------------- | :---------------------------------------------------------------------------- | :------- |
| Battery, 24 V                             | Valence (Lithion)  | [U1-24V24IB](https://www.valence.com/12-and-24v-li-ion-batteries/u1-24v24ib)  | 1        |
| USB-CANbus adapter                        | PEAK               | PCAN-USB, [IPEH-002021](https://www.peak-system.com/PCAN-USB.199.0.html?&L=1) | 1        |
| CAN termination resistor                  | Ixxat              | [1.04.0075.03000](https://www.ixxat.com/products/accessories)                 | 2        |
| Cable                                     | Clearpath Robotics | [030774](./readme_assets/030774_1.pdf)                                        | 1        |
| Mini-ITX with Ubuntu 22.04 and ROS Humble | Clearpath Robotics |                                                                               | 1        |

## Setup

-   `sudo ip link set can0 up type can bitrate 250000`
-   `sudo apt install can-utils`

## Notes

-   Sent
    ```
    cansend can0 18920140#00.00.00.00.00.00.00.00
    ```
-   Response
    ```
    can0  18920140   [8]  00 00 00 00 00 00 00 00
    can0  18924001   [8]  39 01 39 01 00 00 00 00
    ```

    -   39 hex = 57 decimal
    -   57 -40degC = 17degC which seems correct per the current house temperature.

## Reference Material
-   https://github.com/hardbyte/python-can/tree/develop/examples
-   https://python-can.readthedocs.io/en/stable/api.html
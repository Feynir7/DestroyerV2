1. Purpose

DestroyerV2 is software developed to analyze how network protocols behave when a device is exposed to a high volume of traffic.
The project makes it possible to observe:

    how TCP, UDP, ICMP, and HTTP stacks react under abnormal load conditions

    how a router or host handles a large number of simultaneous requests

    which differences emerge between protocols in terms of stability and latency

The program is intended for personal study, local experimentation, and research on the behavior of network protocols.
2. Disclaimer

DestroyerV2 must be used exclusively in:

    private networks owned by the user

    personal devices

    isolated testing environments

    contexts where explicit authorization is provided

The author assumes no responsibility for improper or unauthorized use.
The user is responsible for ensuring that every test complies with applicable laws and is limited to infrastructure under their control.
3. Test Environment and Observed Behavior

The software was tested in a controlled home environment, using:

    a router owned by the author

    an isolated local network

    a dedicated host running the program

During the tests, typical behaviors of a device under abnormal load were observed, including:

    increased internal latency

    temporary slowdowns of the router’s management interface

    reduced ability to handle new connections

    different responses depending on the selected protocol

All tests were performed without involving external networks.
4. Testing Methodology

The testing procedure followed a controlled methodology:

    configuration of an isolated local environment

    launching the program with administrative privileges

    selecting the type of traffic to generate through the interactive menu

    entering the router’s IP address and the port to be analyzed

    running the test for a limited interval

    monitoring the router’s behavior through:

        the device’s web interface

        local diagnostic tools

        system logs

The goal was not to saturate the device, but to observe how it handles abnormal load conditions.
5. Technical Operation of the Script

DestroyerV2 is composed of several modules that use:

    Scapy for generating IP/TCP/ICMP packets

    socket for UDP traffic and raw connections

    httpx for asynchronous HTTP requests

    threading for parallel execution

    asyncio for managing simultaneous requests

    rich for formatted console output

    pyfiglet for the initial banner

    a @timer decorator to measure execution time

The main Dos class contains methods that generate controlled network traffic, each dedicated to a different protocol.
The C_set.py file provides an optional function to compile parts of the code into C using Cython, useful for experimenting with CPU‑bound optimizations.
6. Observed Capabilities

The amount of traffic generated depends on:

    the hardware of the machine running the program

    operating system limits

    local network configuration

    the router’s capabilities

DestroyerV2 therefore allows empirical evaluation of how a device handles a high volume of requests, without providing absolute or comparative performance metrics.
7. Home Router Test Results (Minimum Baseline)

Below are the results obtained on the author’s home router.
This device is relatively slow at handling large numbers of requests, so these values represent minimum baseline observations, not performance limits of the software.

    SYN test: 100 requests processed in approximately 0.1 seconds

    ACK test: 100 requests processed in approximately 0.1 seconds

    ICMP (ping) test: 100 requests processed in approximately 0.1 seconds

    UDP test: 100 requests processed in approximately 0.001 seconds

    HTTP test: 10 requests processed in approximately 0.1 seconds

    Slowloris behavior: full saturation observed after approximately 7–9 minutes

These results reflect the reaction of the specific home router used during testing and should not be generalized to other devices.

Usage:

sudo python3 DestroyerV2.py

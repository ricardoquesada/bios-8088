# IBM PCjr BIOS

![IBM PCjr BIOS dump](https://lh3.googleusercontent.com/QwPdCQFbS4grTTTnEg0aZ1cxE2p2RzSpIH14RtQnXLq9mvLWZoXWBrOtN_WNUs10ocaQ-gvGGSAkjTsx78_RBw0NoiBoYXTEu6hV8MJ68vxkkysJznNz7yVmCDFmdc5h3xHmy23HnPM)


Comments were taken from the [IBM PCjr Technical Reference Guide][0].
Only the comments between brackets and the comments in the BASIC section are from my own.

Includes the the code located from `f000:0000` to `f000:ffff`.

This is WIP. Far from complete. I do it in a _let's see how this code works_ basis.

Using [IDA PRO freeware version][1]

## Hidden diagnostic modes

Detailed description:

*   [IBM PCjr zero-day vulnerability report][2]

TL;DR;:

*   Connect two joysticks
*   Press `Ctrl` + `Alt` + `Insert` keys to enter into diagnostics mode
*   Immediately after that, do:
    *   Press: Joy 1 button B, and Joy 2 buttons A & B for Manufacturing burn-in mode: enters diag loop mode without the diag screen
    *   Press: Joy 1 button A, and Joy 2 buttons A & B for Manufacturing system test mode: enters boot loop. Keeps booting
    *   Press: Joy 1 buttons A & B, and Joy 2 button B for Service loop-post mode: displays all diagnostics options, even if the hardware is not present
    *   Press: Joy 1 buttons A & B, and Joy 2 button A for Service system-test mode
    *   Press: Joy 1 buttons A & B, and joy 2 buttons A & B: enters boot loop with sound test


[0]: https://archive.org/details/IbmPcjrTechnicalReference
[1]: https://www.hex-rays.com/products/ida/support/download_freeware.shtml
[2]: https://retro.moe/2018/01/15/ibm-pcjr-zero-day-data-destroy-vulnerability/

# Strategy: VWAP_EMA_RSI - Trade Rationale and Indicator States

## Strategy Rules:
- Strategy: VWAP crossover confirmed by EMA crossover and RSI not in extreme zone.
- Long Entry: Previous Close <= Previous VWAP_D AND Current Close > Current VWAP_D AND EMA_9 > EMA_21 AND RSI_14 < 75.
- Short Entry: Previous Close >= Previous VWAP_D AND Current Close < Current VWAP_D AND EMA_9 < EMA_21 AND RSI_14 > 25.
- Exits: 1.5% Profit Target, 1.0% Stop Loss, or End-of-Day/Session.

---

## Trade 1: LONG at 2025-06-13 10:40:00-04:00

- **Entry Time:** 2025-06-13 10:40:00-04:00
- **Entry Price:** 528.62
- **Trade Type:** long
- **Exit Time:** 2025-06-13 15:00:00-04:00
- **Exit Price:** 527.20
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -1.42
- **PnL (Net %):** -0.2886%

### Indicator States at Entry:
- **Current Close:** 528.62
- **Current VWAP_D:** 528.55
- **Previous Close:** 528.48
- **Previous VWAP_D:** 528.55
- **EMA_9:** 527.93
- **EMA_21:** 527.68
- **RSI_14:** 65.28

### Entry Rationale:
Entered long because:
- Previous Close (528.48) was <= Previous VWAP_D (528.55).
- Current Close (528.62) crossed > Current VWAP_D (528.55).
- EMA_9 (527.93) was > EMA_21 (527.68).
- RSI_14 (65.28) was < Overbought threshold (75).

---

## Trade 2: LONG at 2025-06-16 09:48:00-04:00

- **Entry Time:** 2025-06-16 09:48:00-04:00
- **Entry Price:** 531.83
- **Trade Type:** long
- **Exit Time:** 2025-06-16 15:00:00-04:00
- **Exit Price:** 534.12
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 2.29
- **PnL (Net %):** 0.4106%

### Indicator States at Entry:
- **Current Close:** 531.83
- **Current VWAP_D:** 531.77
- **Previous Close:** 531.68
- **Previous VWAP_D:** 531.77
- **EMA_9:** 531.93
- **EMA_21:** 531.10
- **RSI_14:** 65.14

### Entry Rationale:
Entered long because:
- Previous Close (531.68) was <= Previous VWAP_D (531.77).
- Current Close (531.83) crossed > Current VWAP_D (531.77).
- EMA_9 (531.93) was > EMA_21 (531.10).
- RSI_14 (65.14) was < Overbought threshold (75).

---

## Trade 3: LONG at 2025-06-16 15:04:00-04:00

- **Entry Time:** 2025-06-16 15:04:00-04:00
- **Entry Price:** 533.97
- **Trade Type:** long
- **Exit Time:** 2025-06-16 15:05:00-04:00
- **Exit Price:** 533.87
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.10
- **PnL (Net %):** -0.0387%

### Indicator States at Entry:
- **Current Close:** 533.97
- **Current VWAP_D:** 533.90
- **Previous Close:** 533.86
- **Previous VWAP_D:** 533.90
- **EMA_9:** 533.98
- **EMA_21:** 533.94
- **RSI_14:** 51.58

### Entry Rationale:
Entered long because:
- Previous Close (533.86) was <= Previous VWAP_D (533.90).
- Current Close (533.97) crossed > Current VWAP_D (533.90).
- EMA_9 (533.98) was > EMA_21 (533.94).
- RSI_14 (51.58) was < Overbought threshold (75).

---

## Trade 4: SHORT at 2025-06-16 15:17:00-04:00

- **Entry Time:** 2025-06-16 15:17:00-04:00
- **Entry Price:** 533.73
- **Trade Type:** short
- **Exit Time:** 2025-06-16 15:18:00-04:00
- **Exit Price:** 533.67
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.06
- **PnL (Net %):** -0.0088%

### Indicator States at Entry:
- **Current Close:** 533.73
- **Current VWAP_D:** 533.90
- **Previous Close:** 533.98
- **Previous VWAP_D:** 533.90
- **EMA_9:** 533.77
- **EMA_21:** 533.80
- **RSI_14:** 47.23

### Entry Rationale:
Entered short because:
- Previous Close (533.98) was >= Previous VWAP_D (533.90).
- Current Close (533.73) crossed < Current VWAP_D (533.90).
- EMA_9 (533.77) was < EMA_21 (533.80).
- RSI_14 (47.23) was > Oversold threshold (25).

---

## Trade 5: LONG at 2025-06-16 15:21:00-04:00

- **Entry Time:** 2025-06-16 15:21:00-04:00
- **Entry Price:** 534.23
- **Trade Type:** long
- **Exit Time:** 2025-06-16 15:22:00-04:00
- **Exit Price:** 534.27
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.04
- **PnL (Net %):** -0.0125%

### Indicator States at Entry:
- **Current Close:** 534.23
- **Current VWAP_D:** 533.90
- **Previous Close:** 533.54
- **Previous VWAP_D:** 533.90
- **EMA_9:** 533.80
- **EMA_21:** 533.80
- **RSI_14:** 61.00

### Entry Rationale:
Entered long because:
- Previous Close (533.54) was <= Previous VWAP_D (533.90).
- Current Close (534.23) crossed > Current VWAP_D (533.90).
- EMA_9 (533.80) was > EMA_21 (533.80).
- RSI_14 (61.00) was < Overbought threshold (75).

---

## Trade 6: SHORT at 2025-06-17 09:32:00-04:00

- **Entry Time:** 2025-06-17 09:32:00-04:00
- **Entry Price:** 532.15
- **Trade Type:** short
- **Exit Time:** 2025-06-17 15:00:00-04:00
- **Exit Price:** 529.46
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 2.69
- **PnL (Net %):** 0.4855%

### Indicator States at Entry:
- **Current Close:** 532.15
- **Current VWAP_D:** 532.16
- **Previous Close:** 532.50
- **Previous VWAP_D:** 532.17
- **EMA_9:** 533.16
- **EMA_21:** 533.54
- **RSI_14:** 30.71

### Entry Rationale:
Entered short because:
- Previous Close (532.50) was >= Previous VWAP_D (532.17).
- Current Close (532.15) crossed < Current VWAP_D (532.16).
- EMA_9 (533.16) was < EMA_21 (533.54).
- RSI_14 (30.71) was > Oversold threshold (25).

---

## Trade 7: SHORT at 2025-06-18 11:58:00-04:00

- **Entry Time:** 2025-06-18 11:58:00-04:00
- **Entry Price:** 531.11
- **Trade Type:** short
- **Exit Time:** 2025-06-18 15:00:00-04:00
- **Exit Price:** 527.74
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 3.37
- **PnL (Net %):** 0.6145%

### Indicator States at Entry:
- **Current Close:** 531.11
- **Current VWAP_D:** 531.14
- **Previous Close:** 531.44
- **Previous VWAP_D:** 531.14
- **EMA_9:** 531.60
- **EMA_21:** 531.62
- **RSI_14:** 36.15

### Entry Rationale:
Entered short because:
- Previous Close (531.44) was >= Previous VWAP_D (531.14).
- Current Close (531.11) crossed < Current VWAP_D (531.14).
- EMA_9 (531.60) was < EMA_21 (531.62).
- RSI_14 (36.15) was > Oversold threshold (25).

---

## Trade 8: LONG at 2025-06-20 09:32:00-04:00

- **Entry Time:** 2025-06-20 09:32:00-04:00
- **Entry Price:** 532.47
- **Trade Type:** long
- **Exit Time:** 2025-06-20 10:45:00-04:00
- **Exit Price:** 527.15
- **Exit Reason:** Stop Loss
- **PnL (Underlying Abs):** -5.32
- **PnL (Net %):** -1.0200%

### Indicator States at Entry:
- **Current Close:** 532.47
- **Current VWAP_D:** 532.15
- **Previous Close:** 532.09
- **Previous VWAP_D:** 532.10
- **EMA_9:** 530.70
- **EMA_21:** 530.09
- **RSI_14:** 73.13

### Entry Rationale:
Entered long because:
- Previous Close (532.09) was <= Previous VWAP_D (532.10).
- Current Close (532.47) crossed > Current VWAP_D (532.15).
- EMA_9 (530.70) was > EMA_21 (530.09).
- RSI_14 (73.13) was < Overbought threshold (75).

---

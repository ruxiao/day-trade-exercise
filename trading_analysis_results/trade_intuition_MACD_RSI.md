# Strategy: MACD_RSI - Trade Rationale and Indicator States

## Strategy Rules:
- Strategy: MACD Crossover with RSI confirmation.
- Long Entry: MACD line crosses above Signal line AND RSI_14 > 50.
- Short Entry: MACD line crosses below Signal line AND RSI_14 < 50.
- Exits: 1.2% Profit Target, 0.8% Stop Loss, or End-of-Day/Session.

---

## Trade 1: SHORT at 2025-06-13 10:04:00-04:00

- **Entry Time:** 2025-06-13 10:04:00-04:00
- **Entry Price:** 528.88
- **Trade Type:** short
- **Exit Time:** 2025-06-13 15:55:00-04:00
- **Exit Price:** 526.11
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** 2.77

### Indicator States at Entry:
- **Current Close:** 528.88
- **Current VWAP_D:** 529.30
- **Previous Close:** 529.18
- **Previous VWAP_D:** 529.31
- **EMA_9:** 529.02
- **EMA_21:** 529.14
- **RSI_14:** 45.05

### Entry Rationale:
Entered short because:
- Previous Close (529.18) was >= Previous VWAP_D (529.31).
- Current Close (528.88) crossed < Current VWAP_D (529.30).
- EMA_9 (529.02) was < EMA_21 (529.14).
- RSI_14 (45.05) was > Oversold threshold (25).

---

## Trade 2: LONG at 2025-06-16 11:02:00-04:00

- **Entry Time:** 2025-06-16 11:02:00-04:00
- **Entry Price:** 534.78
- **Trade Type:** long
- **Exit Time:** 2025-06-16 15:55:00-04:00
- **Exit Price:** 534.18
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** -0.60

### Indicator States at Entry:
- **Current Close:** 534.78
- **Current VWAP_D:** 533.46
- **Previous Close:** 534.73
- **Previous VWAP_D:** 533.46
- **EMA_9:** 534.59
- **EMA_21:** 534.58
- **RSI_14:** 58.91

### Entry Rationale:
Entered long because:
- Previous Close (534.73) was <= Previous VWAP_D (533.46).
- Current Close (534.78) crossed > Current VWAP_D (533.46).
- EMA_9 (534.59) was > EMA_21 (534.58).
- RSI_14 (58.91) was < Overbought threshold (75).

---

## Trade 3: SHORT at 2025-06-17 09:30:00-04:00

- **Entry Time:** 2025-06-17 09:30:00-04:00
- **Entry Price:** 532.42
- **Trade Type:** short
- **Exit Time:** 2025-06-17 15:55:00-04:00
- **Exit Price:** 529.33
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** 3.09

### Indicator States at Entry:
- **Current Close:** 532.42
- **Current VWAP_D:** 532.02
- **Previous Close:** 534.27
- **Previous VWAP_D:** 533.91
- **EMA_9:** 533.64
- **EMA_21:** 533.80
- **RSI_14:** 32.23

### Entry Rationale:
Entered short because:
- Previous Close (534.27) was >= Previous VWAP_D (533.91).
- Current Close (532.42) crossed < Current VWAP_D (532.02).
- EMA_9 (533.64) was < EMA_21 (533.80).
- RSI_14 (32.23) was > Oversold threshold (25).

---

## Trade 4: LONG at 2025-06-18 09:39:00-04:00

- **Entry Time:** 2025-06-18 09:39:00-04:00
- **Entry Price:** 529.36
- **Trade Type:** long
- **Exit Time:** 2025-06-18 15:55:00-04:00
- **Exit Price:** 529.05
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** -0.31

### Indicator States at Entry:
- **Current Close:** 529.36
- **Current VWAP_D:** 529.28
- **Previous Close:** 529.23
- **Previous VWAP_D:** 529.27
- **EMA_9:** 529.15
- **EMA_21:** 529.24
- **RSI_14:** 51.58

### Entry Rationale:
Entered long because:
- Previous Close (529.23) was <= Previous VWAP_D (529.27).
- Current Close (529.36) crossed > Current VWAP_D (529.28).
- EMA_9 (529.15) was > EMA_21 (529.24).
- RSI_14 (51.58) was < Overbought threshold (75).

---

## Trade 5: LONG at 2025-06-20 09:30:00-04:00

- **Entry Time:** 2025-06-20 09:30:00-04:00
- **Entry Price:** 532.52
- **Trade Type:** long
- **Exit Time:** 2025-06-20 10:25:00-04:00
- **Exit Price:** 528.26
- **Exit Reason:** Stop Loss
- **PnL (Underlying):** -4.26

### Indicator States at Entry:
- **Current Close:** 532.52
- **Current VWAP_D:** 532.00
- **Previous Close:** 528.96
- **Previous VWAP_D:** 530.36
- **EMA_9:** 529.80
- **EMA_21:** 529.62
- **RSI_14:** 76.91

### Entry Rationale:
Entered long because:
- Previous Close (528.96) was <= Previous VWAP_D (530.36).
- Current Close (532.52) crossed > Current VWAP_D (532.00).
- EMA_9 (529.80) was > EMA_21 (529.62).
- RSI_14 (76.91) was < Overbought threshold (75).

---

## Trade 6: SHORT at 2025-06-20 10:41:00-04:00

- **Entry Time:** 2025-06-20 10:41:00-04:00
- **Entry Price:** 527.83
- **Trade Type:** short
- **Exit Time:** 2025-06-20 15:55:00-04:00
- **Exit Price:** 526.84
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** 0.99

### Indicator States at Entry:
- **Current Close:** 527.83
- **Current VWAP_D:** 531.01
- **Previous Close:** 528.32
- **Previous VWAP_D:** 531.09
- **EMA_9:** 528.75
- **EMA_21:** 529.07
- **RSI_14:** 32.12

### Entry Rationale:
Entered short because:
- Previous Close (528.32) was >= Previous VWAP_D (531.09).
- Current Close (527.83) crossed < Current VWAP_D (531.01).
- EMA_9 (528.75) was < EMA_21 (529.07).
- RSI_14 (32.12) was > Oversold threshold (25).

---

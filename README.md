# MOAB
Asset allocation switching strategy switching between three assets based on market conditions (TQQQ/SQQQ/UVXY)

# STRATEGY RULES
##  1. Overbought
### Condition:
10 day relative strength index (rsi) of the Nasdaq100 Index is above 80
### Action:
Hold UVXY

## 2. Oversold
### Condition:
10 day relative strength index (rsi) of the Nasdaq100 Index is below 34

OR

2 day relative strength index (rsi) of the Nasdaq100 Index is below 10
### Action:
Hold TQQQ

## 3. Above Long-term Moving Average
### Condition:
Price of Nasdaq100 Index is above its 169-day simple moving average (sma)
### Action:
Hold TQQQ (DCA over 2 Days)

## 4. Above Short-term Moving Average
### Condition:
Price of Nasdaq100 Index is above its 28-day simple moving average (sma)
### Action:
Hold TQQQ

## 5. Default holding
### Condition:
All other statements above are false
### Action:
Hold SQQQ

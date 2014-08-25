text = "X-DSPAM-Confidence:    0.8475";

index = text.find(' ')
print float(text[index:])

import matplotlib.pyplot as plt

x = [200,
210,
220,
230,
240,
250,
260,
270,
280,
290,
300]

y = [176917083,
205597458,
234160875,
271589833,
318876791,
353787250,
392243833,
441055750,
489540000,
544163333,
604745042]

z = [179105720.8,
207337260.0411,
238389714.3848,
272397413.1217,
309494685.5424,
349815860.9375,
393495268.5976,
440667237.8133,
491466097.8752,
546026178.0739,
604481807.7]

plt.figure(figsize=(14, 7))
plt.plot(x, y, marker = 'x', color='red', label='Experimental Time')
plt.plot(x, z, marker = 'o', color='blue', label='Theoretical Time')
plt.xlabel('Number of clients (n)')
plt.ylabel('Times (ns)')
plt.title('Times for different number of clients (for fixed number of servers)')
plt.legend()
plt.show()
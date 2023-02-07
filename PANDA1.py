

import pandas as pd
import pandas as pd

data = {"calories":[-50, 40, 30], "Pulses":[-1, 2, -2]}

df = pd.DataFrame(data, index=["a", "b", "c"])

print(df.abs())


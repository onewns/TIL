# Redux Toolkit



## 1. Action

```javascript
import {createAction} from '@reduxjs/toolkit'

const LOG_IN = "LOG_IN"
const LOG_OUT = "LOG_OUT"

export const logIn = createAction(LOG_IN);

export const logOut = createAction(LOG_OUT);
```


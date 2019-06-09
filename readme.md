WIP. Experiment with urban traffic visualizations

```
./script/run-script script/build-test-image
```

#### Flow data reference

- https://developer.here.com/documentation/traffic/topics/common-acronyms.html
- https://developer.here.com/documentation/traffic/topics/resource-type-functional-class.html

| name | value            |
| ---- | ---------------- |
| RWS  | Roadways         |
| RW   | Roadway          |
| SHP  | Shape            |
| FC   | Functional class |

#### Jam factor reference

| Color  | Description                                             |
| ------ | ------------------------------------------------------- |
| Green  | Free flow of traffic: 0 <= JAM_FACTOR < 4               |
| Yellow | Sluggish flow of traffic: 4 <= JAM_FACTOR < 8           |
| Red    | Slow flow of traffic: 8 <= JAM_FACTOR < 10              |
| Black  | Traffic stopped flowing or road closed: JAM_FACTOR = 10 |

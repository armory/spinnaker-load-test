This generates read load for API endpoints. It's dependent on generated write/queue load from this project here: https://github.com/ajordens/spinnaker-performance


Run the following to build the container

```
bin/build
```

Then run

```
bin/run [gate_api]
```
To run the container.  Where `[gate_api]` is your gate endpoint. Go to http://localhost:8089 and run the load test

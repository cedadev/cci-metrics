# cci-metrics

This is a Flask app which uses CEDA's [prometheus wrapper](https://github.com/cedadev/ceda-unittest-prometheus-wrapper) to run multiple sets of unit tests and show the results of them in a webpage. Waitress to manage the WSGI server.

## List of Unit Tests
Currently, the following suites of unit tests are run and outputted to the Flask app:
- [CCI FTP](https://github.com/cedadev/cci-odp-ops-tests-ftp)
- [CCI CSW](https://github.com/cedadev/cci-odp-ops-tests-csw)
- [CCI OPeNDAP](https://github.com/cedadev/cci-odp-ops-tests-tds-opendap)
- [CCI ESGF Search](https://github.com/cedadev/cci-odp-ops-tests-esgf-search)
- [CCI THREDDS OGC](https://github.com/cedadev/tds_ogc_services_check)

In addition to this, the production CCI Metrics Grafana service also hosts metrics for `cp4cds-metrics`, however the execution of these tests is managed elsewhere. The reason for merging these metrics with CCI is so they run on the external JASMIN cloud; this will still allow for the metrics service to function even if JASMIN has a serious downtime (this is because the external cloud is on a separate network to the rest of JASMIN).

The Flask app creates a number of instances of `TestDataContainer`, used to store the test cases, test names (of each of the test cases) and an overall service name. The code for the `TestDataContainer` is currently sitting in a different branch to master (`multiple-test-classes`) in the `ceda-unittest-prometheus-wrapper` in order to not harm other implementations of that repository. A list of these containers are passed to the app factory function in that repo to launch the Flask app.

## Usage
When installing with the associated playbook, use Circusd to start, stop and restart this Flask app:

`circusctl start cci-metrics`

The logs for this app will be stored in `/var/log/cci-metrics`. 

Go for full [kube prometheus](https://github.com/prometheus-operator/kube-prometheus) stack (prometheus operator, prometheus,node exporter,blackbox exporter) or just for [Prometheus operator](https://github.com/prometheus-operator/prometheus-operator?tab=readme-ov-file#helm-chart)

```bash
# install only the operator via helm https://github.com/prometheus-operator/prometheus-operator?tab=readme-ov-file#helm-chart
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install [RELEASE_NAME] prometheus-community/kube-prometheus-stack

# need for  lstat /var/log/pods/monitoring_prom-prometheus-node-exporter...no such file or directory error
helm install prom prometheus-community/kube-prometheus-stack -n monitoring --set prometheus-node-exporter.hostRootFsMount.enabled=false

# check grafana
# get password for admin user
kubectl -n monitoring get secrets prom-grafana -ojsonpath="{.data.admin-password}" | base64 -d
kubectl -n monitoring port-forward svc/prom-grafana 8088:80
```


## Alternatives

Jira Service Management and Compass
Atlassian offers two option to migrate from Opsgenie: JSM or Compass.

Grafana OnCall
Part of Grafana Cloud IRM (Incident response & management).Delivers customized notifications via Slack, Microsoft Teams, Telegram, SMS, phone calls, email, and more. 

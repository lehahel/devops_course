#!/bin/bash
kubectl apply \
  -f app/deploy/service.yaml \
  -f app/deploy/deployment.yaml \
  -f app/deploy/gateway.yaml \
  -f app/deploy/egress.yaml \
  -f nginx/deploy/service.yaml \
  -f nginx/deploy/deployment.yaml \
  -f nginx/deployt/gateway.yaml

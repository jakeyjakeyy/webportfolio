#!/bin/bash

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Build docker images
echo -e "${YELLOW}Step 1: Building docker images...${NC}"
docker rmi $(docker images -q)
docker-compose build --no-cache

# Step 2: Tag frontend and backend images
echo -e "${YELLOW}Step 2: Tagging frontend and backend images...${NC}"
docker tag "webportfolio_frontend:latest" "docker.io/jakerichards/webportfolio_frontend"
docker tag "webportfolio_backend:latest" "docker.io/jakerichards/webportfolio_backend"

# Step 3: Push frontend/backend images
echo -e "${YELLOW}Step 3: Pushing frontend/backend images...${NC}"
docker push "docker.io/jakerichards/webportfolio_frontend"
docker push "docker.io/jakerichards/webportfolio_backend"

# Step 4: SSH into server
echo -e "${YELLOW}Step 4: SSH into server...${NC}"
ssh jakerichards <<EOF
    # Step 5: Stop old docker images
    echo -e "${YELLOW}Step 5: Stopping old docker images...${NC}"
    cd "webportfolio"
    docker-compose down

    # Step 6: Remove old images
    echo -e "${YELLOW}Step 6: Removing old images...${NC}"
    docker rmi \$(docker images -q)

    # Step 7: Update local files
    echo -e "${YELLOW}Step 7: Updating local files...${NC}"
    git stash
    git pull
    git stash pop

    # Step 8: Deploy
    echo -e "${YELLOW}Step 8: Deploying...${NC}"
    docker-compose up -d
EOF

echo -e "${GREEN}Deployment completed successfully.${NC}"

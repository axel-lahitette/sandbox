aws-vault exec gl-gekko -- aws cloudformation package --template ./lambda-cf.yml --s3-bucket axel-project-bucket --output yaml > packaged-lambda-template.yml
aws-vault exec gl-gekko -- aws s3 ls
aws-vault exec gl-gekko -- aws s3 ls axel-project-bucket
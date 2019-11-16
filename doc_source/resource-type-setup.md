# Setting Up Your Environment for Developing Resource Providers<a name="resource-type-setup"></a>

Before you can develop resource providers, you'll need to set up your developer environment, including the CloudFormation CLI\.

Currently, add\-ins are available for the following languages:
+ Java

Or, if you're using another language, you can install the CloudFormation CLI directly\.

## Setting Up Your Java Environment \(macOS\)<a name="resource-type-setup-java"></a>

### Prerequisites<a name="resource-type-setup-java-prereqs"></a>
+ Python version 3\.6 or above
+ Any JDK 8, and Maven
+ [AWS Command Line Interface](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-cli.html) for access to `aws cloudformation` commands\.
+ Your choice of Java IDE

  The [Walkthrough: Develop a Resource Provider](resource-type-walkthrough.md) walkthrough uses the Community Edition of the [IntelliJ IDEA](https://www.jetbrains.com/idea/)\.
+ [AWS Serverless Application Model Command Line Interface](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) \(AWS SAM CLI\)
**Note**
[Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html) requires Docker as a prerequisite for testing your resource provider locally\.

In addition, the code generated by the CloudFormation CLI uses [Lombok](https://projectlombok.org/), which requires support in IDEs for some syntax highlighting to work\. For the best development experience, it is recommended you install Lombok support in your IDE\.

### To Set Up Your Java Environment \(macOS\)<a name="resource-type-setup-java-steps"></a>

Complete the following steps to install and configure the tools needed to develop resource providers using Java\.

1. Install Homebrew

   First, install [Homebrew](https://brew.sh/), an open\-source package manager for macOS\. You'll use Homebrew to install additional development requirements\.

1. Next, use Homebrew to install Maven, Python, and the AWS Command Line Interface \(AWS CLI\)\.

   ```
   $ brew update
   $ brew install maven python awscli
   ```

1. Install the CloudFormation CLI using the following command:

   ```
   pip install cloudformation-cli

1. Install the Java Plug\-in for CloudFormation CLI using the following command:

   ```
   pip install cloudformation-cli-java-plugin
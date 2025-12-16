from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""


class BuildInvoke_dotnet10_cookiecutter_aws_sam_hello_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet10/hello"
    should_test_lint = False

class BuildInvoke_dotnet10_cookiecutter_aws_sam_hello_native_aot_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet10/hello-native-aot"
    should_test_lint = False

class BuildInvoke_dotnet10_cookiecutter_aws_sam_hello_dotnet_pt(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet10/hello-pt"
    should_test_lint = False


class BuildInvoke_dotnet10_cookiecutter_aws_sam_quick_start_s3_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet10/s3"
    should_test_lint = False


class BuildInvoke_dotnet10_cookiecutter_aws_sam_quick_start_sns_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet10/sns"
    should_test_lint = False


class BuildInvoke_dotnet10_cookiecutter_aws_sam_quick_start_sqs_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet10/sqs"
    should_test_lint = False


class BuildInvoke_dotnet10_cookiecutter_aws_sam_hello_step_functions_sample_app(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet10/step-func"
    should_test_lint = False


class BuildInvoke_dotnet10_cookiecutter_aws_sam_quick_start_cloudwatch_events_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet10/cw-event"
    should_test_lint = False


class BuildInvoke_dotnet10_cookiecutter_aws_from_scratch_dotnet(BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase):
    use_container = False
    directory = "dotnet10/scratch"
    should_test_lint = False


class BuildInvoke_dotnet10_cookiecutter_aws_sam_quick_start_web_dotnet(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    use_container = False
    directory = "dotnet10/web"
    should_test_lint = False


#
# Image templates
#


class BuildInvoke_image_dotnet10_cookiecutter_aws_sam_hello_dotnet_lambda_image(
    BuildInvokeBase.DotNetCoreExtraRerunBuildInvokeBase
):
    directory = "dotnet10/hello-img"
    should_test_lint = False

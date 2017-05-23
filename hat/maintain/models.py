from django.db import models


# 记录节点信息，用来对测试用例分组，本次迭代中不进行操作
class NodeHierarchy(models.Model):
    node_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    details = models.TextField()
    parent_id = models.IntegerField(null=True)
    input_code = models.CharField(max_length=20)
    node_order = models.IntegerField()
    type_choice = {
        (0, '根节点'),
        (1, '子节点'),
        (2, '叶子节点')
    }
    # 只有叶子节点下可以添加对应测试用例
    node_type = models.IntegerField(choices=type_choice, default=0)


# 对应测试用例进行版本分类，有单独维护界面，在批量复制的时候提供自动替换
class Version(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    detail = models.TextField()


# 对测试用例主机信息进行分类，有单独维护界面，在批量复制时提供自动替换
class HostPort(models.Model):
    id = models.AutoField(primary_key=True)
    host_port = models.CharField(max_length=50)
    description = models.TextField()


# 测试用例核心，抛弃参数与参数值组合功能，单一测试用例中包含对应路径、参数、预期结果等信息。
# 在执行测试用例时直接获取对应json数据中的值，直接与预期结果进行比对，判断测试用例是否通过。
class TestCase(models.Model):
    case_id = models.AutoField(primary_key=True)
    node_id = models.ForeignKey(NodeHierarchy)
    case_name = models.CharField(max_length=100)
    host_port = models.ForeignKey(HostPort)
    path = models.CharField(max_length=200)
    method_choice = (
        (0, 'GET'),
        (1, 'POST'),
        (2, 'PUT'),
        (3, 'DELETE'),
    )
    method = models.IntegerField(choices=method_choice, default=0)
    json_data = models.TextField()
    cookie = models.TextField()
    version = models.ForeignKey(Version)
    expect_result = models.TextField()

    def getUrl(self):
        print(self.__dict__)
        print(self.host_port.__dict__)
        return "http://" + self.host_port.host_port + self.path

    def getName(self):
        return self.case_name
    def getExpect(self):
        return self.expect_result



# class Param(models.Model):
#     param_id = models.AutoField(primary_key=True)
#     param_name = models.CharField(max_length=40)
#     case_id = models.ForeignKey(TestCase)
#     value = models.CharField(max_length=200)
#     type_choice = (
#         (0, 'PARAM'),
#         (1, 'PATH'),
#     )
#     type = models.IntegerField(choices=type_choice, default=0)

# 记录测试用例执行结果，其中包含测试用例信息、真实数据、执行结果和执行信息。
# 其中执行信息用来对执行结果进行分组，生成每次执行的测试用例报告。
class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(TestCase)
    case_name = models.CharField(max_length=100)
    expect_result = models.TextField()
    real_result = models.TextField()
    test_result = models.BooleanField()
    execute_date = models.DateField(auto_now=True)
    execute_time = models.IntegerField()
    execute = models.CharField(max_length=30)
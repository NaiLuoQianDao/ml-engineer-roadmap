def test_create_and_read_file(tmp_path):
    # 1. 查看 pytest 提供的临时文件夹
    print("临时文件夹:", tmp_path)

    # 2. 构造文件路径
    file_path = tmp_path / "hello.txt"

    # 3. 创建并写入文件
    file_path.write_text("Hello, Python!", encoding="utf-8")

    # 4. 读取文件
    content = file_path.read_text(encoding="utf-8")

    # 5. 检查内容
    assert content == "Hello, Python!"

def test_numbers_file(tmp_path):
    file_path = tmp_path / 'numbers.txt'
    file_path.write_text('12\n34')
    content = file_path.read_text()
    assert content.splitlines() == ['12', '34']
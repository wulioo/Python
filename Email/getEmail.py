# -*- codeing = utf-8 -*-
# @Time : 2020/11/24 7:13 下午

import poplib
import base64
import re
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from loguru import logger


class Email():
    def __init__(self, email, password, pop_server):
        self.email = email
        self.password = password
        self.pop_server = pop_server
        self.msg = self.get_email()
        self.udid = self.print_info()

    def get_email(self):
        # 链接到POP3服务器
        server = poplib.POP3(self.pop_server)

        # 打开调试，打印出会话内容，可选
        # server.set_debuglevel(1)

        # 打印POP3服务器的欢迎文字，可选
        print(server.getwelcome().decode('utf-8'))

        # 进行身份认证
        server.user(self.email)
        server.pass_(self.password)

        # stat() 返回邮件数量和占用空间，返回两个。
        mail_total, total_size = server.stat()
        # print('Messages: %s. Size: %s' % (mail_total, total_size))

        # list 返回所有邮件编号，第一个是返回状态信息，第二个是列表
        resp, mails, octets = server.list()
        # logger.info("邮件列表" + str(mails))
        # 获取最新一封邮件, 注意索引号从1开始,最后是最新的
        list = []
        for i in range(1, len(mails)):
            try:
                # lines存储了邮件的原始文本的每一行,
                resp, lines, octets = server.retr(i)
                # 可以获得整个邮件的原始文本:
                msg_content = b'\r\n'.join(lines).decode('utf-8')
                # 解析成massage对象
                msg = Parser().parsestr(msg_content)
                list.append(msg)
            except Exception as f:
                print(f)
        # logger.info(list)
        # 关闭连接
        server.quit()
        return list


    # -- 解析头部信息
    def print_info(self):
        udid_list = []
        for msg in self.msg:
            logger.info("================解析Email==================")
            name = ''
            for header in ['From', 'To', 'Subject']:
                value = msg.get(header, '')
                if value:
                    if header == 'From':
                        try:
                            hdr, addr = parseaddr(value)
                            name = self.decode_str(hdr)
                            value = u'{}<{}>'.format(name, addr)
                        except Exception as e:
                            logger.info(e)
                    elif header == 'To':
                        value = self.decode_str(value)
                    elif header == 'Subject':
                        value = self.decode_str(value)
                logger.info('{}: {}'.format(header, value))
            if name != '蒲公英团队':
                continue
            else:
                udid = self.get_content(msg)
                udid_list.append(udid)
        return udid_list



    # ----解析文本内容
    def get_content(self, msg):
        for part in msg.walk():
            content_type = part.get_content_type()
            charset = self.guess_charset(msg, part)
            if part.get_filename() != None:  # 如果有附件，则直接跳过
                continue
            email_content_type = ''
            content = ''
            if content_type == 'text/plain':
                email_content_type = 'text'
            elif content_type == 'text/html':
                # print('html 格式 跳过')
                # continue  # 不要html格式的邮件
                email_content_type = 'html'
            if charset:
                try:
                    content = part.get_payload(decode=True).decode(charset)
                except AttributeError:
                    print('type error')
                except LookupError:
                    print("unknown encoding: utf-8")
            if email_content_type == '':
                continue  # 如果内容为空，也跳过
            # print(email_content_type + ' ------------------------------------------- \n  ' + content)
            udid = self.conten_txt(content)
            return udid

    # --截取文本内容'UDID[\s].[\s](.*?)</p>'
    def conten_txt(self, content):

        udid = re.findall('UDID[\s].[\s](.*?)</p>', content)[0]
        logger.info('Content: {}'.format(udid))
        return udid

    # --获取编码字符集
    def guess_charset(self, msg, part):
        charset = msg.get_charset()
        if charset is None:
            content_type = part.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset

    # -- email字符串解析
    def decode_str(self, s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value


if __name__ == '__main__':
    e = Email('zhengdh@huabo.tech', 'Aa1234bb', 'pop.exmail.qq.com')

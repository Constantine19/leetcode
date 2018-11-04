class Solution(object):
    def pre_process_email(self, email):
        local_name = ''
        domain = ''
        for i in range(len(email)):
            if email[i] == '@':
                local_name = email[0:i]
                domain = email[i:]
        local_name = local_name.replace('.', '')

        for i in range(len(local_name)):
            if local_name[i] == '+':
                local_name = local_name[0:i]
                break
        final_email = local_name + domain
        return final_email

    def numUniqueEmails(self, emails):
        pre_processed_emails = []
        unique_emails = []

        for email in emails:
            pre_processed_emails.append(self.pre_process_email(email))

        for unique_email in pre_processed_emails:
            if unique_email not in unique_emails:
                unique_emails.append(unique_email)

        return len(unique_emails)

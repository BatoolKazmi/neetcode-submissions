class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []

        for i in range(len(emails)):
            local, domain = emails[i].split("@")

            clean_local = emails[i].split("+")[0].replace(".","")

            final = f"{clean_local}@{domain}"
            
            if final not in res:
                res.append(final)
        
        return len(res)


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        dist = 0

        def addRoom(r, c):
            if (c < 0 or r < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1):
                return
            q.append([r,c])
            visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1
        
        
        
        
        
        
        
        
        
        
        # 📧 Sample Email to BMO – Request for Guidance on Account Access Transition
        # Subject: Guidance Needed: Transition of Access for University Club Business Account

        # Dear BMO Team,

        # I hope you're doing well.

        # My name is Batool Kazmi, and I’m a member of a university club that holds a business bank account with BMO. Currently, only one individual has access to the account, but they will be leaving the club shortly. We would like to ensure a smooth and secure transition of account access to the incoming executive(s).

        # Could you please advise us on the steps we need to take to:

        # Transfer signing authority or account access to new club members
        # Provide any required documentation (e.g., meeting minutes, ID, club registration)
        # Ensure compliance with BMO’s policies for student organizations or non-profits
        # We would appreciate any forms, instructions, or guidance you can share to help us complete this process properly.

        # Thank you for your support, and we look forward to your response.

        # Warm regards,
        # Batool Kazmi
        # [Phone Number]
        # [Email Address]
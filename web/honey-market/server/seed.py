from app import *
from settings import *
from sqlalchemy.exc import IntegrityError
import os

def seed_data():

    # Delete old artifacts
    if os.path.isfile(DATABASE_FILE):
        os.remove(DATABASE_FILE)

    # Create the initial database
    with app.app_context():
        db.create_all()

        # Create a user ADMIN first
        admin =  Users(name=ADMIN_USERNAME,btcaddr="bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6" # :D
            , display_name="HoneyMaster", profile_pic="flag.jpg").setPassword(ADMIN_PASSWORD)
        db.session.add(admin)
        db.session.commit()
        
        # Seed some illegal products of HoneyMaster
        db.session.add_all([
            Products(title="Goggle",bestFame=True, 
                brief="The world’s most dominant search and ad-tech company, known for its global data collection and AI research. Contact now for their database dumps.", picture="goggle.png", 
                content="12.4TB of behavioral gold. Includes real user search logs, synced browser histories, Gmail threads, Drive contents, and high-value autofill exports. Categorized by obsession — medical, political, fetish, and corporate. Ideal for profiling, phishing, or just knowing what humanity dreams of at 3AM.\n\nNo duplicates. No mercy.", price="7331", author=admin.id),
            Products(title="PineApple", bestFame=True, 
                brief="A luxury tech brand famous for its sleek smartphones, encrypted messaging, and walled-garden ecosystem, whom information we have!", picture="pineapple.png", 
                content="Decrypted iCloud slices. Full account dumps: photos, location tracks, voice memos, iMessage threads. Several celebrity devices included. Internal device schematics for unreleased models. Bonus: Siri command logs and bug reports marked “never fix.” Privacy is their brand — now it’s your product.", price="1336", author=admin.id),
            Products(title="Microhard", bestFame=True, 
                brief="A software behemoth behind the most used desktop OS and enterprise productivity tools worldwide but not for long, since we know where they're going ;)", picture="microhard.png", 
                content="Well, not as hard as they thought LOL! Because this one includes Outlook inboxes, SharePoint leaks, and 24GB of internal Teams comms. Access credentials for Azure DevOps pipelines and private Windows telemetry dashboards. Also includes “accidental” screen recordings from internal demo calls. If you sell ransomware kits, this is your entry key.", price="1200", author=admin.id),
            Products(title="Netfix",bestFame=True,
                brief="A global leader in digital streaming, producing original content. Data includes their upcoming plans and source code.", picture="netfix.png", 
                content="2.1 million user profiles. Includes watch history, location traces, payment metadata, and parental control bypass logs. Unreleased pilots, marketing projections, and algorithm tuning scripts also available. Great for OSINT, blackmail, or just spoiling Season 4 before release.", price="1336.99", author=admin.id),
            Products(title="Amazin",bestFame=True,
                brief="A global e-commerce and logistics empire, with its own data centers, cloud services, and even satellites. Contact us now for their employees records.", picture="amazen.png", 
                content="Amazin indeed! Because these leaks will \"amaze\" yall since it contains Customer purchase history, shipping addresses, Prime watch behavior, and Alexa audio files (“Delete everything I said” = not honored). Video footage from warehouse cams included. For those in retail surveillance or psychological targeting — this is platinum stock.", price="999", author=admin.id),
            Products(title="MetaBook",bestFame=True,
                brief="The largest social mesh platform, monetizing user connections and behaviors at an unprecedented scale. 500M leaked records are awaiting.", picture="meta.png", 
                content="DM archives, deleted post logs, shadow profiles, full ad targeting parameters, and internal moderation memos. Faces, friends, locations. Time-stamped and indexed. Data includes cross-platform ID resolution with Instaspam and Snaptrash. And for the icing on the cake, Zuckerberg's selfies as well.\n\nTheir network. Your weapon.", price="1000", author=admin.id),
            Products(title="Haxorone",bestFame=True,
                brief="A vulnerability disclosure platform connecting ethical hackers with corporations seeking bug bounties, we didn't do bounties, we did better.", picture="haxorone.png", 
                content="Private vulnerabilities submitted by top-tier researchers. Unpatched CVEs, payout negotiation logs, and internal Slack debates. Cross-referenced with vendor fix timelines. Excellent for 0day development or shaming campaigns. Contains high-profile gov and financial sector targets.\n\nOh bbooiizz! Hack the hackers they said!", price="1038", author=admin.id),
            Products(title="BugKrow", picture="bugkrow.png",
                brief="A crowdsourced security platform offering real-time vulnerability reporting from global researchers and we hacked their database.", 
                content="Vuln submission archive. High severity bugs flagged as “Informational.” PDF scopes, customer contacts, and payment discrepancies. Includes mirrored private programs never meant to go public. A buffet of bugs they tried to suppress. For serious exploit brokers only.", price="1300", author=admin.id),
            Products(title="PecanCorp",picture="pecan.png",
                brief="An infamous 1337 corporation responsible for CTF challenges in Australia.", 
                content="Full backend source of recent CTF events — including challenge flags, solve stats, and admin-only walkthroughs from the upcoming PECAN+ 2025. User submissions, partial solves, and team rankings available for tampering or extortion. Includes internal staff Slack chats, shady sponsorship agreements, and a leaked doc titled “How to Pretend Your Challenge Isn’t Broken.”\n\nIronically, they didn’t protect their own scoreboard. GG.", price="2025", author=admin.id),
            Products(title="l33t.Inc",picture="1337Corp.png",
                brief="Powerfully l33t organization that everyone is scared of, it hosts PII and various data which are all parts of this leak.", 
                content="Top-tier intel: full identity packs (PII, biometrics, passports, etc.), blackmail archives, financials, and internal logs discussing “containment” scenarios. Backdoor access tokens to partner darknet services included. This isn’t a breach — it’s controlled chaos.\n\nBuy it only if you’re ready for attention.", price="2025", author=admin.id),
            Products(title="Intelli", 
                picture="Intelli.png",brief="A chip manufacturing giant at the heart of modern computing, AI, and processors. Breaches include their future plan and sketches for the upcoming processors.",
                content="Unreleased microcode, errata logs, architectural diagrams. Debug interfaces for current-gen CPUs, and internal docs discussing covert access pathways.\n\nIf you understand firmware-level exploitation, this is your playground. Signed NDA not required — just crypto.", price="892", author=admin.id),
            Products(title="Flindi University",picture="Flindi.png",
                brief="One of the biggest South Australian institutions with many juicy student's data.", 
                content="Student records, disciplinary reports, unpublished theses, and military-adjacent research. Internal communications show lax security and hilariously poor password habits. Dump includes Wi-Fi access logs and internal VPN credentials. Perfect for lateral movement testing.", price="1309", author=admin.id),
            Products(title="Wakanda.gov",picture="wakanda.png",
                brief="PII of Wakandanians of the most technologically advanced country in the world, data also includes vibranium-powered systems.", 
                content="State-level research on vibranium-based materials, energy systems, and stealth technologies. Includes classified diplomatic cables, internal security architecture, and real-time location data for key assets. Highest bidder only. No refunds. No questions.\n\n\n UPDATE: After the recent incident of Thanos snapping his damn fingers, the price skyrocketed.", price="1337.09", author=admin.id),
            Products(title="Toracle",picture="toracle.png",
                brief="Enterprise database titan and cloud services provider, breach includes legacy systems and government contracts.",bestFame=True, 
                content="Client databases, support case archives, unpatched OracleDB vulns, and contract negotiation files. Found an email thread about “accidental root access” to a bank. You’ll know what to do. Leak is 89% PDFs. The rest is weapon-grade bureaucracy.", price="1337", author=admin.id)
        ])

        db.session.add(
            HoneySecrets(
                flag=CAN_BE_FLAG,
                message_of_the_day=MOTD_QUOTE)
        )

        db.session.commit()

if __name__ == "__main__":
    seed_data()
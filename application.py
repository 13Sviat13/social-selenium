from services import SocialNetworkScraper

if __name__ == '__main__':
    service = SocialNetworkScraper()

    title = "My blog is ghost"
    content = "I will delete this soon"
    service.social_network_post(title, content)
    driver = service.create_driver()

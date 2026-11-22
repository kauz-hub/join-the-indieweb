# 12. Decentralized social media

[Home](../README.md) · [Next: discovery](13-discovery.md)

Decentralization distributes the operation of a network among multiple providers or participants. Federation lets independently run services communicate using a shared protocol. Open-source software alone doesn't make a service decentralized. And decentralized doesn't automatically mean safe, private, or independent of large operators.

## Choose a network by what you like doing

| Platform | Main activity | Network or protocol |
|---|---|---|
| [Mastodon](https://joinmastodon.org/) | Microblogging and conversation | ActivityPub |
| [Pixelfed](https://pixelfed.org/) | Photos, albums and visual updates | ActivityPub |
| [Lemmy](https://join-lemmy.org/) | Topic communities and discussions | ActivityPub |
| [PeerTube](https://joinpeertube.org/) | Video channels | ActivityPub |
| [Misskey](https://misskey-hub.net/) | Creative microblogging | ActivityPub |
| [Friendica](https://friendi.ca/) | General social networking | ActivityPub and other connections |
| [WriteFreely](https://writefreely.org/) | Longer-form writing | ActivityPub federation |
| [Bluesky](https://bsky.app/) | Microblogging and custom feeds | AT Protocol |
| [Matrix](https://matrix.org/) | Messaging and chat rooms | Matrix protocol |

Matrix is a messaging network, not a public social feed. Bluesky is not a native ActivityPub platform. Cross-protocol bridges exist, but compatibility and visibility vary.

## How the fediverse works

[ActivityPub](https://www.w3.org/TR/activitypub/) allows compatible servers to exchange posts and interactions. For example, a Mastodon user may follow a Pixelfed account, even though they use different software. Not all features translate between applications, and servers can limit or block federation with others.

To get started, choose a server from the platform's official directory. Read its rules, moderation policies, funding model, registration conditions and supported features. You generally don't need to operate your own server.

- [Mastodon server directory](https://joinmastodon.org/servers) and [documentation](https://docs.joinmastodon.org/).
- [Pixelfed](https://pixelfed.org/) includes server discovery and documentation.
- [Lemmy instances](https://join-lemmy.org/instances), including [Lemmy.World](https://lemmy.world/).
- [PeerTube](https://joinpeertube.org/) provides information on joining video instances.

Your account address identifies both you and your home server. Migration support differs across software. For instance, moving a Mastodon account can move followers where supported, but old posts do not automatically become posts on the new account. Export what you can.

## Bluesky and the AT Protocol

Bluesky uses [AT Protocol](https://atproto.com/), which separates several network roles, including personal data servers, network indexing and application views. It supports domain handles and aims to provide account portability and choice of feeds and moderation services. The Bluesky app and much of the network infrastructure may still depend on centralized operators in practice.

Sign up through [Bluesky](https://bsky.app/), browse feeds and configure moderation preferences. If you own a domain, follow the [official domain handle guide](https://bsky.social/about/blog/3-6-2023-domain-names-as-handles-in-bluesky). A domain handle establishes a connection to that domain; it does not by itself host your social account or preserve all your data.

## Your own website is still your home base

Keep original photos and writing on your website and share links on your social accounts. Put social profile links on your About page. Consider [POSSE and feeds](06-publishing-and-feeds.md), and optionally [Bridgy Fed](https://fed.brid.gy/) to connect supported networks. You can also join ordinary forums, use email, or maintain a blogroll instead of running any social account.

Public posts may be copied by other servers. Understand the limits of deletion, direct-message confidentiality, moderation and data export before posting sensitive information.

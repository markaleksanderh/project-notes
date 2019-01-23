import React, { Component } from 'react'
import Post from './Post'
import { Query } from 'react-apollo'
import gql from 'graphql-tag'

const POST_QUERY = gql`
  {
    allPosts{
      edges{
        node{
          id
          title
          body
        }
      }
    }
  }
`


class PostList extends Component {
  render() {
    return (
    <Query query={POST_QUERY}>
      {({loading, error, data})=>{
        if (loading) return <div>Fetching...</div>
        if (error) {
          console.log(error)
          return <div>Error</div>
        }
        const postsToRender = data.allPosts
        console.log(postsToRender)
        return (

          <div>
            {postsToRender.map(post => <Post key={post.id} post={post} />)}
          </div>
        )
      }}
    </Query>
    )
  }
}

export default PostList

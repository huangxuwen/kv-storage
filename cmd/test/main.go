package main

import (
	"fmt"

	pb "code.avlyun.org/grpc/kv-storage"
	"github.com/golang/protobuf/proto"
)

func main() {
	q := &pb.SearchRequest{Rule: []*pb.RuleUnit{
		{Space: "foo", Index: 0},
		{Space: "bar", Index: 1},
	}, Queries: []*pb.Query{
		{Keys: []string{"k1", "k2"}},
		{Keys: []string{"t1", "t2"}},
	}}

	bs, _ := proto.Marshal(q)
	fmt.Println(bs)
	q2 := pb.SearchRequest{}
	proto.Unmarshal(bs, &q2)
	fmt.Println(q2.String())
}
